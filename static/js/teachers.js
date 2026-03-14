const inputName = document.getElementById("teacher-name")
const inputColleagues = document.getElementById("teacher-colleagues")

function addTeacher() {
    const colleagues = inputColleagues.value.split(",").map(v => v.trim()).filter(v => v !== "").map(Number)

    console.log(fetch("api/teachers", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify({'id': 1, 'name': inputName.value, 'colleagues': colleagues})
    }).then(r => r.json()))

    inputName.value = ''
    inputColleagues.value = ''
}