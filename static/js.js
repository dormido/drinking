function changeLanguage() {
    var language = document.getElementById("language").value;
    window.location.href = "/?language=" + language;
}