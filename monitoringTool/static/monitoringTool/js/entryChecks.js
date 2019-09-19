// Run Timeout session
timeOutSession('expires');

// Timeout session method
function timeOutSession(expires) {
    // Expiring time (sec)
    var expiresIn = 1800000;
	var homePage = "https://podsmanagementapp.azurewebsites.net/";

	// Timer
	setTimeout(function(){
		console.log("Time for redirect");
		sessionStorage.clear();
	
		window.location.replace(homePage); // Redirect		
	}, expiresIn);
}


// TEST: Checks active status using cookie life spam
function checkActiveStatusWithCookie(username) {

	alert('Before');
	var user = getCookie(username);

	if (user = "" || user == null) {
		//var newPage = "https://" + window.location.host;
		var newPage = "https://www.google.com";
		// Redirect
		window.location.replace(newPage);
	} else {

	}

	// Timer
	setTimeout(function(){
		checkActiveStatus(username); // Recall function
	}, 5000);
}
