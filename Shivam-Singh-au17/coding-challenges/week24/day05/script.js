
const NextBtn = document.getElementById("nextBtn")
const PrevBtn = document.getElementById("prevBtn")
const question = document.getElementById("question")
const opt01 = document.getElementById("option01")
const opt02 = document.getElementById("option02")
const opt03 = document.getElementById("option03")
const opt04 = document.getElementById("option04")



async function getData() {

    try {
        const response = await fetch(`https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple`)
        const jsonData = await response.json()
        return jsonData.results
    }
    catch (e) {
        return e.message
    }
}



NextBtn.addEventListener("click", async () => {

    let data = await getData()

    data.map((item) => {
        question.innerHTML = item.question
        opt01.innerHTML = item.correct_answer
        opt02.innerHTML = item.incorrect_answers[0]
        opt03.innerHTML = item.incorrect_answers[1]
        opt04.innerHTML = item.incorrect_answers[2]
    })

})


PrevBtn.addEventListener("click", async () => {

    let data = await getData()

    data.map((item) => {
        question.innerHTML = item.question
        opt01.innerHTML = item.correct_answer
        opt02.innerHTML = item.incorrect_answers[0]
        opt03.innerHTML = item.incorrect_answers[1]
        opt04.innerHTML = item.incorrect_answers[2]
    })

})

