"""
appManda.py — Mandarin Flashcards (CLOUD VERSION)
-----------------------------------------
Same idea as the Kost app, but for studying Mandarin, and with PROFILES:

  Stage 1: the app password  (the front door)
  Stage 2: pick a profile    (like choosing a user on Netflix)
  Stage 3: that profile's own password

The 250 words are grouped into 7 CHAPTERS. Study a chapter, then take its
test. Test scores are saved per profile, per chapter.

There is also a Dev Console: a master key that can read and delete any
profile. Its entrance is deliberately faint on the profile screen, and it
needs its own separate password.

Data is saved per profile on GitHub via cloud_store.py.
Setup instructions: read README.md BEFORE deploying.
"""

import random

import streamlit as st

from wordsManda import (
    THEMES, CHAPTERS, TEST_LENGTH, PASS_MARK,
    all_words, words_for_theme, theme_names,
    chapter_words, get_chapter, chapter_label,
)
from cloud_storeManda import load_data, save_data, get_profile, blank_profile
from profilesManda import (
    get_profiles, check_app_password, check_profile_password,
    check_dev_password, display_name, profile_avatar,
)

st.set_page_config(page_title="Mandarin Flashcards 汉字", page_icon="🀄", layout="wide")


# ---------------------------------------------------------------------------
# A little CSS. The important bit is .st-key-devgate: Streamlit turns a
# container's key into a CSS class, which lets us make ONE button almost
# invisible without touching any of the others.
# ---------------------------------------------------------------------------
st.markdown("""
<style>
  .st-key-devgate button {
      opacity: 0.05 !important;
      border: none !important;
      background: transparent !important;
      box-shadow: none !important;
      transition: opacity .25s ease;
  }
  .st-key-devgate button:hover { opacity: 0.30 !important; }
  .st-key-devgate button:focus { opacity: 0.55 !important; }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Session state — Streamlit forgets everything between clicks unless we
# store it here.
# ---------------------------------------------------------------------------
def init_state():
    defaults = {
        "gate_passed": False,
        "profile": None,
        "dev_mode": False,
        "picking": None,
        "dev_prompt": False,     # is the hidden dev password box showing?
        "card_index": 0,
        "flipped": False,
        "study_chapter": None,
        "quiz_word": None,
        "quiz_options": [],
        "quiz_answered": False,
        "test_chapter": None,    # which chapter test is running
        "test_qs": [],
        "test_i": 0,
        "test_results": [],
        "test_done": False,
        "test_picked": None,
        "test_saved": False,   # guard: record each attempt exactly once
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_state()


def reset_test_state():
    st.session_state.test_chapter = None
    st.session_state.test_qs = []
    st.session_state.test_i = 0
    st.session_state.test_results = []
    st.session_state.test_done = False
    st.session_state.test_picked = None
    st.session_state.test_saved = False


def build_test(pool):
    """
    Build one chapter test: TEST_LENGTH questions drawn from that chapter's
    words, each with 4 possible meanings.

    The wrong options are picked from the WHOLE word list, not just this
    chapter, so a test never accidentally gives the answer away by running
    out of plausible choices.
    """
    everything = all_words()
    picked = random.sample(pool, min(TEST_LENGTH, len(pool)))
    questions = []
    for word in picked:
        distractors = random.sample(
            [w["english"] for w in everything if w["english"] != word["english"]], 3
        )
        options = [word["english"]] + distractors
        random.shuffle(options)
        questions.append({"word": word, "options": options})
    return questions


# ---------------------------------------------------------------------------
# STAGE 1 — the front door
# ---------------------------------------------------------------------------
if not st.session_state.gate_passed:
    st.title("🔒 Mandarin Flashcards")
    st.caption("Enter the app password to continue.")
    pw = st.text_input("App password", type="password")
    if st.button("Enter"):
        if check_app_password(pw): "4536"
          st.session_state.gate_passed = True
            st.rerun()
        else:
            st.error("Wrong password.")
    st.stop()


# ---------------------------------------------------------------------------
# Connect to storage (only after the front door, so strangers never touch it)
# ---------------------------------------------------------------------------
try:
    data = load_data()
except Exception as e:
    st.error(f"Failed to connect to cloud storage (GitHub). Details: {e}")
    st.info("Double-check 'github_token' and 'github_repo' in Secrets — see README.md.")
    st.stop()

PROFILES = get_profiles()

if not PROFILES:
    st.warning("No profiles are set up yet. Add at least one in Secrets — see README.md.")
    st.stop()


# ---------------------------------------------------------------------------
# STAGE 2 & 3 — pick a profile, then unlock it with its own password
# ---------------------------------------------------------------------------
if st.session_state.profile is None and not st.session_state.dev_mode:
    st.title("Who's studying?")
    st.caption("Pick your profile. Each one keeps its own progress.")

    keys = list(PROFILES.keys())
    cols = st.columns(min(4, len(keys)))
    for i, key in enumerate(keys):
        with cols[i % len(cols)]:
            st.markdown(
                f"<div style='font-size:56px;text-align:center;line-height:1'>{profile_avatar(key)}</div>",
                unsafe_allow_html=True,
            )
            if st.button(PROFILES[key]["display"], key=f"pick_{key}", use_container_width=True):
                st.session_state.picking = key
                st.session_state.dev_prompt = False
                st.rerun()

    # Stage 3 — password for the chosen profile
    if st.session_state.picking:
        who = st.session_state.picking
        st.divider()
        st.subheader(f"{profile_avatar(who)} {display_name(who)}")
        ppw = st.text_input(f"Password for {display_name(who)}", type="password", key="ppw")
        c1, c2 = st.columns([1, 3])
        if c1.button("Unlock"):
            if check_profile_password(who, ppw):
                st.session_state.profile = who
                st.session_state.picking = None
                st.rerun()
            else:
                st.error("Wrong password for this profile.")
        if c2.button("Back"):
            st.session_state.picking = None
            st.rerun()

    # ---------------------------------------------------------------------
    # The faint Dev Console entrance. It is a real button, just styled to
    # almost disappear (see the CSS at the top). It still needs the dev
    # password, so hiding it is a nicety, not the actual lock.
    # ---------------------------------------------------------------------
    st.write("")
    st.write("")
    left, mid, right = st.columns([6, 1, 6])
    with mid:
        with st.container(key="devgate"):
            if st.button("·", key="devbtn"):
                st.session_state.dev_prompt = not st.session_state.dev_prompt
                st.rerun()

    if st.session_state.dev_prompt:
        st.divider()
        st.caption("Dev Console — master key. Requires its own password.")
        dpw = st.text_input("Dev password", type="password", key="dpw")
        d1, d2 = st.columns([1, 3])
        if d1.button("Unlock Console"):
            if check_dev_password(dpw):
                st.session_state.dev_mode = True
                st.session_state.dev_prompt = False
                st.rerun()
            else:
                st.error("Wrong dev password.")
        if d2.button("Hide"):
            st.session_state.dev_prompt = False
            st.rerun()

    st.stop()


# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
if st.session_state.dev_mode:
    st.sidebar.title("🛠️ Dev Console")
    st.sidebar.caption("Master key — you can see and delete every profile.")
    PAGES = ["Dev Console"]
else:
    who = st.session_state.profile
    st.sidebar.title(f"{profile_avatar(who)} {display_name(who)}")
    st.sidebar.caption("Mandarin Flashcards · 250 words · 7 chapters")
    PAGES = ["Chapters", "Flashcards", "Quiz", "Browse Words", "My Progress"]

page = st.sidebar.radio("Menu", PAGES)

if st.sidebar.button("Switch profile / Sign out"):
    st.session_state.profile = None
    st.session_state.dev_mode = False
    st.session_state.picking = None
    st.session_state.dev_prompt = False
    st.session_state.card_index = 0
    st.session_state.flipped = False
    st.session_state.quiz_word = None
    st.session_state.quiz_options = []
    st.session_state.quiz_answered = False
    reset_test_state()
    st.rerun()


# ---------------------------------------------------------------------------
# PAGE: DEV CONSOLE
# ---------------------------------------------------------------------------
if page == "Dev Console":
    st.title("🛠️ Dev Console")
    st.warning(
        "This is a master key. It can read and delete every profile's progress. "
        "Anyone you share the dev password with gets the same power."
    )

    total_words = len(all_words())
    stored = data.get("profiles", {})

    st.subheader("All profiles")
    for key in PROFILES:
        p = stored.get(key, blank_profile())
        known = len(p.get("known", []))
        seen = p.get("seen", 0)
        correct = p.get("correct", 0)
        wrong = p.get("wrong", 0)
        chapters = p.get("chapters", {})
        passed = sum(1 for c in chapters.values() if c.get("passed"))
        accuracy = f"{round(correct / (correct + wrong) * 100)}%" if (correct + wrong) else "—"

        with st.container(border=True):
            c0, c1, c2, c3, c4 = st.columns([1.5, 1, 1, 1, 1])
            c0.markdown(f"### {profile_avatar(key)} {PROFILES[key]['display']}")
            c1.metric("Known", f"{known}/{total_words}")
            c2.metric("Chapters passed", f"{passed}/{len(CHAPTERS)}")
            c3.metric("Cards seen", seen)
            c4.metric("Quiz accuracy", accuracy)

            with st.expander(f"Details — {PROFILES[key]['display']}"):
                st.write("**Known characters**")
                st.write("  ".join(p.get("known", [])) if known else "_None yet._")
                st.write("**Chapter tests**")
                if chapters:
                    for cn, res in sorted(chapters.items(), key=lambda x: int(x[0])):
                        mark = "✅" if res.get("passed") else "❌"
                        st.write(f"{mark} {chapter_label(int(cn))} — best {res.get('best', 0)}% "
                                 f"· {res.get('attempts', 0)} attempt(s)")
                else:
                    st.caption("No tests taken yet.")

    # -----------------------------------------------------------------------
    # Delete tools. Every one of these is irreversible inside the app, so each
    # needs an explicit tick first.
    # -----------------------------------------------------------------------
    st.divider()
    st.subheader("🗑️ Delete progress")

    target = st.selectbox("Profile", list(PROFILES.keys()), key="del_target",
                          format_func=lambda k: PROFILES[k]["display"])
    what = st.radio(
        "What should be deleted?",
        ["Known words only", "Quiz scores only", "Chapter test results only",
         "Everything for this profile", "Remove this profile's record entirely"],
        index=0, key="del_what",
    )
    confirm = st.checkbox(f"Yes — delete «{what}» for {PROFILES[target]['display']}",
                          key="del_confirm")

    if st.button("Delete", type="primary", key="del_go", disabled=not confirm):
        data.setdefault("profiles", {})
        prof = data["profiles"].get(target, blank_profile())

        if what == "Known words only":
            prof["known"] = []
            data["profiles"][target] = prof
        elif what == "Quiz scores only":
            prof["correct"] = 0
            prof["wrong"] = 0
            prof["seen"] = 0
            data["profiles"][target] = prof
        elif what == "Chapter test results only":
            prof["chapters"] = {}
            data["profiles"][target] = prof
        elif what == "Everything for this profile":
            data["profiles"][target] = blank_profile()
        else:  # remove record entirely
            data["profiles"].pop(target, None)

        save_data(data)
        st.success(f"Done — {what.lower()} deleted for {PROFILES[target]['display']}.")
        st.rerun()

    with st.expander("☢️ Wipe every profile"):
        st.caption("This empties the whole database. Only the GitHub commit history can bring it back.")
        typed = st.text_input("Type DELETE ALL to confirm", key="wipe_text")
        if st.button("Wipe everything", key="wipe_go", disabled=(typed != "DELETE ALL")):
            data["profiles"] = {}
            save_data(data)
            st.success("All profiles wiped.")
            st.rerun()

    st.caption(
        "Recovery: every save is a commit in your GitHub repo, so an older version of "
        "mandarin_data.json can always be restored from the commit history."
    )
    st.stop()


# ---------------------------------------------------------------------------
# A learner is signed in from here on
# ---------------------------------------------------------------------------
me = get_profile(data, st.session_state.profile)
me.setdefault("known", [])
me.setdefault("chapters", {})
ALL = all_words()


def is_known(hanzi):
    return hanzi in me["known"]


def toggle_known(hanzi):
    if hanzi in me["known"]:
        me["known"].remove(hanzi)
    else:
        me["known"].append(hanzi)
    save_data(data)


def chapter_result(n):
    """This profile's best result for a chapter, or None if never attempted."""
    return me["chapters"].get(str(n))


# ---------------------------------------------------------------------------
# PAGE: CHAPTERS  (study list + end-of-chapter test)
# ---------------------------------------------------------------------------
if page == "Chapters":

    # ---------------- a test is in progress ----------------
    if st.session_state.test_chapter is not None and not st.session_state.test_done:
        n = st.session_state.test_chapter
        qs = st.session_state.test_qs
        i = st.session_state.test_i
        q = qs[i]

        st.title(f"📝 {chapter_label(n)} — Test")
        st.progress(i / len(qs))
        st.caption(f"Question {i + 1} of {len(qs)}  ·  pass mark {PASS_MARK}%")

        st.markdown(
            f"<div style='text-align:center;font-size:72px;padding:14px'>{q['word']['hanzi']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='text-align:center;color:#B4342A;font-size:19px;margin-bottom:16px'>"
            f"{q['word']['pinyin']}</div>",
            unsafe_allow_html=True,
        )

        picked = st.session_state.test_picked
        for j, opt in enumerate(q["options"]):
            if st.button(opt, key=f"t_{n}_{i}_{j}", use_container_width=True,
                         disabled=picked is not None):
                st.session_state.test_picked = opt
                st.session_state.test_results.append({
                    "hanzi": q["word"]["hanzi"],
                    "pinyin": q["word"]["pinyin"],
                    "answer": q["word"]["english"],
                    "picked": opt,
                    "right": opt == q["word"]["english"],
                })
                st.rerun()

        if picked is not None:
            last = st.session_state.test_results[-1]
            if last["right"]:
                st.success("Correct!")
            else:
                st.error(f"Not quite — {q['word']['hanzi']} means **{q['word']['english']}**.")

            label = "See results ▶" if i + 1 >= len(qs) else "Next question ▶"
            if st.button(label, use_container_width=True):
                st.session_state.test_picked = None
                if i + 1 >= len(qs):
                    st.session_state.test_done = True
                else:
                    st.session_state.test_i = i + 1
                st.rerun()

        if st.button("Quit test"):
            reset_test_state()
            st.rerun()
        st.stop()

    # ---------------- test finished: show the result ----------------
    if st.session_state.test_done:
        n = st.session_state.test_chapter
        results = st.session_state.test_results
        right = sum(1 for r in results if r["right"])
        score = round(right / len(results) * 100) if results else 0
        passed = score >= PASS_MARK

        st.title(f"📝 {chapter_label(n)} — Result")
        if passed:
            st.success(f"Passed! {right}/{len(results)} correct — {score}%")
            st.balloons()
        else:
            st.error(f"{right}/{len(results)} correct — {score}%. You need {PASS_MARK}% to pass.")

        # Save the attempt, keeping the best score. Passing once stays passed.
        # The test_saved guard matters: Streamlit re-runs this whole block on
        # every click (including "Retake"), and without it each click would
        # count as another attempt.
        if not st.session_state.test_saved:
            prev = me["chapters"].get(str(n), {"best": 0, "attempts": 0, "passed": False})
            me["chapters"][str(n)] = {
                "best": max(prev.get("best", 0), score),
                "attempts": prev.get("attempts", 0) + 1,
                "passed": prev.get("passed", False) or passed,
            }
            save_data(data)
            st.session_state.test_saved = True

        wrong = [r for r in results if not r["right"]]
        if wrong:
            st.subheader("Words to review")
            for r in wrong:
                st.write(f"**{r['hanzi']}** ({r['pinyin']}) = {r['answer']}  "
                         f"— you chose _{r['picked']}_")
        else:
            st.subheader("Perfect score — nothing to review 🎉")

        c1, c2 = st.columns(2)
        if c1.button("Retake test", use_container_width=True):
            st.session_state.test_qs = build_test(chapter_words(n))
            st.session_state.test_i = 0
            st.session_state.test_results = []
            st.session_state.test_done = False
            st.session_state.test_picked = None
            st.session_state.test_saved = False
            st.rerun()
        if c2.button("Back to chapters", use_container_width=True):
            reset_test_state()
            st.rerun()
        st.stop()

    # ---------------- the chapter list ----------------
    st.title("Chapters")
    st.caption(f"Study the words in a chapter, then take its test. You need {PASS_MARK}% to pass.")

    for ch in CHAPTERS:
        words = chapter_words(ch["n"])
        known = sum(1 for w in words if is_known(w["hanzi"]))
        res = chapter_result(ch["n"])

        with st.container(border=True):
            top = st.columns([3, 1.2, 1.2])
            top[0].markdown(f"### {ch['icon']} {chapter_label(ch['n'])}")
            top[0].caption(" · ".join(ch["themes"]))
            top[1].metric("Words known", f"{known}/{len(words)}")
            if res:
                badge = "✅ Passed" if res["passed"] else "❌ Not yet"
                top[2].metric("Best score", f"{res['best']}%", badge)
            else:
                top[2].metric("Best score", "—", "Not taken")

            st.progress(known / len(words) if words else 0)

            b1, b2 = st.columns(2)
            if b1.button("📖 Study these words", key=f"study_{ch['n']}", use_container_width=True):
                st.session_state.study_chapter = ch["n"]
                st.session_state.card_index = 0
                st.session_state.flipped = False
                st.rerun()
            if b2.button("📝 Take the test", key=f"test_{ch['n']}", use_container_width=True):
                st.session_state.test_chapter = ch["n"]
                st.session_state.test_qs = build_test(words)
                st.session_state.test_i = 0
                st.session_state.test_results = []
                st.session_state.test_done = False
                st.session_state.test_picked = None
                st.session_state.test_saved = False
                st.rerun()

    passed_count = sum(1 for c in me["chapters"].values() if c.get("passed"))
    st.divider()
    st.metric("Chapters passed", f"{passed_count} / {len(CHAPTERS)}")


# ---------------------------------------------------------------------------
# PAGE: FLASHCARDS
# ---------------------------------------------------------------------------
elif page == "Flashcards":
    st.title("Flashcards")

    chapter_choices = ["All words"] + [chapter_label(c["n"]) for c in CHAPTERS]
    default_i = 0
    if st.session_state.study_chapter:
        want = chapter_label(st.session_state.study_chapter)
        if want in chapter_choices:
            default_i = chapter_choices.index(want)
        st.session_state.study_chapter = None

    c1, c2 = st.columns([2, 1])
    choice = c1.selectbox("Chapter", chapter_choices, index=default_i)
    hide_known = c2.checkbox("Hide words I know", value=False)

    if choice == "All words":
        deck = ALL
    else:
        num = int(choice.split()[1])
        deck = chapter_words(num)

    if hide_known:
        deck = [w for w in deck if not is_known(w["hanzi"])]

    if not deck:
        st.success("You know every word here! 🎉 Uncheck 'Hide words I know' to review them.")
        st.stop()

    idx = st.session_state.card_index % len(deck)
    card = deck[idx]
    st.caption(f"Card {idx + 1} of {len(deck)} · {card['theme']}")

    with st.container(border=True):
        st.markdown(
            f"<div style='text-align:center;padding:26px 10px'>"
            f"<div style='font-size:82px;line-height:1.1'>{card['hanzi']}</div>"
            + (
                f"<div style='font-size:24px;color:#B4342A;margin-top:10px'>{card['pinyin']}</div>"
                f"<div style='font-size:20px;color:#555;margin-top:4px'>{card['english']}</div>"
                if st.session_state.flipped else
                "<div style='color:#999;margin-top:14px'>Tap Flip to see the meaning</div>"
            )
            + "</div>",
            unsafe_allow_html=True,
        )

    b1, b2, b3, b4 = st.columns(4)
    if b1.button("◀ Previous", use_container_width=True):
        st.session_state.card_index = (idx - 1) % len(deck)
        st.session_state.flipped = False
        st.rerun()
    if b2.button("🔄 Flip", use_container_width=True):
        st.session_state.flipped = not st.session_state.flipped
        me["seen"] = me.get("seen", 0) + 1
        save_data(data)
        st.rerun()
    if b3.button("Next ▶", use_container_width=True):
        st.session_state.card_index = (idx + 1) % len(deck)
        st.session_state.flipped = False
        st.rerun()
    label = "✅ Known" if is_known(card["hanzi"]) else "☆ Mark known"
    if b4.button(label, use_container_width=True):
        toggle_known(card["hanzi"])
        st.rerun()


# ---------------------------------------------------------------------------
# PAGE: QUIZ  (quick practice, any word, no pass mark)
# ---------------------------------------------------------------------------
elif page == "Quiz":
    st.title("Quick Quiz")
    st.caption("Random words from everywhere. For a graded test, use Chapters.")

    def new_question():
        word = random.choice(ALL)
        wrong = random.sample([w for w in ALL if w["english"] != word["english"]], 3)
        options = [word] + wrong
        random.shuffle(options)
        st.session_state.quiz_word = word
        st.session_state.quiz_options = options
        st.session_state.quiz_answered = False

    if st.session_state.quiz_word is None:
        new_question()

    word = st.session_state.quiz_word
    st.markdown(f"<div style='text-align:center;font-size:74px;padding:18px'>{word['hanzi']}</div>",
                unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;color:#B4342A;font-size:20px;margin-bottom:14px'>"
                f"{word['pinyin']}</div>", unsafe_allow_html=True)

    for i, opt in enumerate(st.session_state.quiz_options):
        if st.button(opt["english"], key=f"opt_{i}", use_container_width=True,
                     disabled=bool(st.session_state.quiz_answered)):
            if opt["english"] == word["english"]:
                me["correct"] = me.get("correct", 0) + 1
                st.session_state.quiz_answered = "right"
            else:
                me["wrong"] = me.get("wrong", 0) + 1
                st.session_state.quiz_answered = "wrong"
            save_data(data)
            st.rerun()

    if st.session_state.quiz_answered == "right":
        st.success(f"Correct! {word['hanzi']} ({word['pinyin']}) = {word['english']}")
    elif st.session_state.quiz_answered == "wrong":
        st.error(f"Not quite. {word['hanzi']} ({word['pinyin']}) = {word['english']}")

    if st.session_state.quiz_answered:
        if st.button("Next question ▶", use_container_width=True):
            new_question()
            st.rerun()

    correct, wrong = me.get("correct", 0), me.get("wrong", 0)
    if correct + wrong:
        st.caption(f"Score so far: {correct} correct · {wrong} wrong · "
                   f"{round(correct / (correct + wrong) * 100)}% accuracy")


# ---------------------------------------------------------------------------
# PAGE: BROWSE WORDS
# ---------------------------------------------------------------------------
elif page == "Browse Words":
    st.title("Browse Words")
    search = st.text_input("Search (characters, pinyin, or English)")
    theme = st.selectbox("Theme", ["All themes"] + theme_names())

    deck = ALL if theme == "All themes" else words_for_theme(theme)
    if search:
        s = search.lower()
        deck = [w for w in deck
                if s in w["hanzi"].lower() or s in w["pinyin"].lower() or s in w["english"].lower()]

    st.caption(f"{len(deck)} words")
    # NOTE: a few characters appear in more than one theme (e.g. 鱼 in Food and
    # Animals), so the button key must include the row number — two buttons
    # sharing a key crashes the page.
    for i, w in enumerate(deck):
        c1, c2, c3, c4 = st.columns([1, 1.4, 2, 1])
        c1.markdown(f"<span style='font-size:28px'>{w['hanzi']}</span>", unsafe_allow_html=True)
        c2.write(w["pinyin"])
        c3.write(w["english"])
        mark = "✅" if is_known(w["hanzi"]) else "☆"
        if c4.button(mark, key=f"br_{i}_{w['hanzi']}"):
            toggle_known(w["hanzi"])
            st.rerun()


# ---------------------------------------------------------------------------
# PAGE: MY PROGRESS
# ---------------------------------------------------------------------------
elif page == "My Progress":
    st.title("My Progress")

    total = len(ALL)
    known = len(me["known"])
    correct, wrong = me.get("correct", 0), me.get("wrong", 0)
    passed = sum(1 for c in me["chapters"].values() if c.get("passed"))

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Words known", f"{known}/{total}")
    c2.metric("Chapters passed", f"{passed}/{len(CHAPTERS)}")
    c3.metric("Cards seen", me.get("seen", 0))
    c4.metric("Quiz accuracy",
              f"{round(correct / (correct + wrong) * 100)}%" if correct + wrong else "—")

    st.progress(known / total if total else 0)

    st.subheader("Chapter tests")
    for ch in CHAPTERS:
        res = chapter_result(ch["n"])
        if res:
            mark = "✅" if res["passed"] else "❌"
            st.write(f"{mark} **{chapter_label(ch['n'])}** — best {res['best']}% "
                     f"· {res['attempts']} attempt(s)")
        else:
            st.write(f"⬜ **{chapter_label(ch['n'])}** — not taken yet")

    st.subheader("By theme")
    for t in THEMES:
        words = t["words"]
        got = sum(1 for w in words if is_known(w[0]))
        st.write(f"**{t['zh']} · {t['en']}** — {got}/{len(words)}")
        st.progress(got / len(words) if words else 0)

    st.divider()
    if st.button("Reset my progress"):
        data["profiles"][st.session_state.profile] = blank_profile()
        save_data(data)
        st.success("Your progress has been reset.")
        st.rerun()
