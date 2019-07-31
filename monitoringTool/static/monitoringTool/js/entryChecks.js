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
    console.log("**now: " + now);
    console.log("**expiresTime: " + expiresTime);
    console.log("**Diff: expiresTime - now: " + diff);

	if ((now > expiresTime) || (expiresTime == "" || expiresTime == null)) {
	    console.log("Time for redirect");
	    sessionStorage.clear();

		var newPage = "http://127.0.0.1:8000/";
		window.location.replace(newPage); // Redirect
	}

	// Timer
	setTimeout(function(){
		checkActiveStatusWithSession(expires); // Recall function
	}, 15000);
}


// Checks active status using cookie life spam
function checkActiveStatusWithCookie(username) {

	alert('Before');
	var user = getCookie(username);
	//var user = getCookie(username);
	//console.log('Checking cookie...' + user);
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
//    });
