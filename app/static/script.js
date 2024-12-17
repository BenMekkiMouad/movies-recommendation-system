async function getRecommendations() {
    const movie = document.getElementById("movie-input").value;
    const response = await fetch(`/recommend?movie_name=${movie}&num_recommendations=5`);
    const data = await response.json();
    const recommendations = data.recommendations;

    const recommendationsList = document.getElementById("recommendations");
    recommendationsList.innerHTML = "";
    recommendations.forEach((rec) => {
        const li = document.createElement("li");
        li.textContent = rec;
        recommendationsList.appendChild(li);
    });
}
