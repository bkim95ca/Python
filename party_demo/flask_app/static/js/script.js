console.log("script is linked")

function addParty(event) {
    event.preventDefault()
    // console.log("Function Linked")
    const partyForm = document.querySelector("#new_party")
    const tableBody = document.querySelector("#table_body")
    // console.log(partyForm)
    // console.log(tableBody)
    let formData = new FormData(partyForm)
    fetch('/api/parties/create', {
        method : 'post',
        body : formData
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            tableBody.innerHTML += `
            <tr>
                    <td>${data.form.what}</td>
                    <td>${data.form.location}</td>
                    <td>${data.form.date}</td>
                    <td>${data.form.all_ages == 1 ? "Yes" : "No"}</td>
                    <td>${data.planner}</td>
                    <td>
                        <a href="/parties/${data.form.party_id}">View</a>
                        <a href="/parties/${data.form.party_id}/edit">Edit</a>
                        <a href="/parties/${data.form.party_id}/delete">Delete</a>
                    </td>
                </tr>
            
            
            `
        })
        .catch(err => console.log(err))
}