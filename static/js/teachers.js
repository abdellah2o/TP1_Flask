// Show teachers
function displayTeachers() {
    const table = document.getElementById("data-table");

  fetch("api/teachers")
    .then(r => r.json())
    .then(result => {
      if (!result || result.length === 0) {
        table.innerHTML = "<tr><td>Aucun résultat.</td></tr>"
        return
      }

      const keys = Object.keys(result[0])
      let html = "<thead><tr>"
      keys.forEach(key =>  html += ("<th>" + key + "</th>"))
      html += "</tr></thead>"

      html += "<tbody>"
      result.forEach(elem => {
        html += "<tr>"
        keys.forEach(key => {
          html += "<td>" + elem[key] + "</td>"
        })
        html += "</tr>"
      })
      html += "</tbody>"

      table.innerHTML = html
    })
}
document.addEventListener("DOMContentLoaded", () => displayTeachers())


// Add teacher
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
    displayTeachers()
}

// Delete teacher
const inputId = document.getElementById("teacher-id")

function deleteTeacher() {
    console.log(fetch("api/teachers/" + inputId.value, {
        method: "DELETE",
        headers: {'Content-Type': 'application/json'}
    }))

    inputId.value = ''
    displayTeachers()
}

// Update teacher
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
    displayTeachers()
}