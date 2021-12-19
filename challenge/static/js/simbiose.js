

try {
    document.getElementById("new_employee").onclick = createEmployee;
    } catch {}
try {
    document.getElementById("new_recommendation").onclick = createRecommendation;
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