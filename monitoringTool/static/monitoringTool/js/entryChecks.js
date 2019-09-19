// Active status check
checkActiveStatusWithSession('expires');

// Checks active status using session life spam
function checkActiveStatusWithSession(expires) {
    // Expiring time
    var expiresTime = sessionStorage.getItem(expires);

    // Current time
	var now = new Date();

	if (now.getHours() != 0 || now.getMinutes() != 0) {
		now = now.getMinutes() * now.getHours();
	} else {
		now = now.getMinutes();
	}

    var diff =  expiresTime - now;
    //console.log("**now: " + now);
    console.log("**expiresTime: " + expiresTime);
    //console.log("**Diff: expiresTime - now: " + diff);

	if ((now > expiresTime) || (expiresTime == "" || expiresTime == null)) {
	    console.log("Time for redirect");
	    sessionStorage.clear();

		var newPage = "https://podsmanagementapp.azurewebsites.net/";
		window.location.replace(newPage); // Redirect
	}

	// Timer
	setTimeout(function(){
		checkActiveStatusWithSession(expires); // Recall function
	}, 15000);
}

// Timeout session method
function timeOutSession() {
	console.log("timeOutSession()");

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
