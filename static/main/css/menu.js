menu.onclick = function menu()	{

	var x = document.getElementById('myTopnav');

	if (x.className === "topnav") {
		x.className += " responsive";
	}
	else {
		x.className = "topnav";
	}

}