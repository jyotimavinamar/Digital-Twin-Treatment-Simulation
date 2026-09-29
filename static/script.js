function showLoader() {
    document.getElementById("loader").style.display = "block";
}

function showChart(med, therapy) {
    const ctx = document.getElementById("comparisonChart");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Medication", "Therapy"],
            datasets: [{
                label: "Recovery Score",
                data: [med, therapy],
                backgroundColor: ["#ff7675", "#55efc4"]
            }]
        }
    });
}
