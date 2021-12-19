

try {
    document.getElementById("new_employee").onclick = createEmployee;
    } catch {}
try {
    document.getElementById("new_recommendation").onclick = createRecommendation;
    } catch {}

try {
    document.getElementById("new_team").onclick = createTeam;
    } catch {}

try {
    document.getElementById("new_employee_team").onclick = createEmployeeTeam;
    } catch {}

function createEmployee() {
    let name = document.getElementById("full_name").value;
    let email = document.getElementById("email").value;
    let recommendedBy = document.getElementById("recommended_by").value;

    let url = `createemployee?name=${name}&email=${email}&recommended=${recommendedBy}`;
    fetch(url).then((response) => {
        if (response.status === 500) {
            alert("id inválido");
        }
        window.location.href = "/"
    });
}

function createRecommendation() {
    let name = document.getElementById("candidate_name").value;
    let email = document.getElementById("candidate_email").value;
    let recommendedBy = document.getElementById("recommended_by").value;

    let url = `createrecommendation?name=${name}&email=${email}&recommended=${recommendedBy}`;
    fetch(url).then((response) => {
        if (response.status === 500) {
            alert("id inválido");
        }
        window.location.href = "/recommendations";
    });
}

function createTeam() {
    let name = document.getElementById("team_name").value;

    let url = `createteam?name=${name}`;
    fetch(url).then((response) => {
        window.location.href = "/teams";
    });
}

function createEmployeeTeam() {
    let team = document.getElementById("team_id").value;
    let employee = document.getElementById("employee_id").value;

    let url = `createemployeeteam?team=${team}&employee=${employee}`;
    fetch(url).then((response) => {
        if (response.status === 500) {
            alert("id inválido");
        }
        window.location.href = "/teams";
    });
}