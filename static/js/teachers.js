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
        body: JSON.stringify({'id': -1, 'name': inputName.value, 'colleagues': colleagues})
    }).then(r => r.json()))

    inputName.value = ''
    inputColleagues.value = ''
}


const inputId = document.getElementById("teacher-id")

function deleteTeacher() {
    console.log(fetch("api/teachers/" + inputId.value, {
        method: "DELETE",
        headers: {'Content-Type': 'application/json'}
    }))

    inputId.value = ''
}


const inputNamePut = document.getElementById("teacher-name-put")
const inputColleaguesPut = document.getElementById("teacher-colleagues-put")
const inputIdPut = document.getElementById("teacher-id-put")

function updateTeacher() {
    const colleaguesPut = inputColleaguesPut.value.split(",").map(v => v.trim()).filter(v => v !== "").map(Number)

    console.log(fetch("api/teachers/" + inputIdPut.value, {
        method: "PUT",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'id': -1, 'name': inputNamePut.value, 'colleagues': colleaguesPut})
    }).then(r => r.json()))

    inputNamePut.value = ''
    inputColleaguesPut.value = ''
    inputIdPut.value = ''
}