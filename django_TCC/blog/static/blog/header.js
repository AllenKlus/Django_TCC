document.getElementById("burger_icon").addEventListener("touchend", myFunction)
document.getElementById("burger_icon").addEventListener("touchstart", myFunction)
function myFunction() {
  var x = document.getElementById("responsive_links");
  var y = document.getElementById("main");
  if (x.style.display === "flex") {
    x.style.display = "none";
    y.style.paddingTop = "100px"
  } else {
    x.style.display = "flex";
    y.style.paddingTop = "150px"
  }
}
