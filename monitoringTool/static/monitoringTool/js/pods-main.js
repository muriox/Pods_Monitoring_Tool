/**
	Pods main .js
*/
$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });  

	/** Form Process Functions */
	// Declarations
	loginAndSignupDisplayControl("#spanSignup", "#podsSignup", "#podsLogin");
	loginAndSignupDisplayControl("#spanLogin", "#podsLogin", "#podsSignup");

	loginFieldDisplayControl("#forgetPassCheck", "#loginpassDiv", "#loginCheck", "#submitFormOne", "#formOneTitle");
	loginFieldDisplayControl("#loginCheck", "#loginpassDiv", "#forgetPassCheck", "#submitFormOne", "#formOneTitle");

	// Login form process
	podsPostFormOne("#submitFormOne");
	// Sign up form process
	podsPostFormTwo("#submitFormTwo");


	/**---------------------------------
	---------- FUNCTIONS ---------------
	------------------------------------ */
	// Login and Sign up display function
	function loginAndSignupDisplayControl(clicked, showDiv, checkDisplay) {
		$(clicked).click(function(){
			$(showDiv).show();
			$(checkDisplay).hide();
		});
	}

	// Login password display/hide
	function loginFieldDisplayControl(clicked, passField, controlledDiv, formButton, formTitle) {
		$(clicked).click(function(){
			var isVisible = $(passField).is( ":visible" );
			var loginStr = "Login";
			var resetStr = "Reset";
			var currentButtonVal = $(formButton).text();
			var currentTitleVal = $(formTitle).text();

			if (isVisible) {
				//alert("Vis" + $( "#submitFormOne" ).text());
				$(passField).hide();
				$(clicked).hide();
				$(controlledDiv).show();
				$(formButton).text(currentButtonVal.replace(loginStr, resetStr));
				$(formTitle).text(currentTitleVal.replace(loginStr, resetStr));
			} else {
				//alert("Vis" + $( "#submitFormOne" ).text());
				$(passField).show();
				$(clicked).hide();
				$(controlledDiv).show();
				$(formButton).text(currentButtonVal.replace(resetStr, loginStr));
				$(formTitle).text(currentTitleVal.replace(resetStr, loginStr));
			}
		});
	}

	/** -----------------AJAX DEPENDING FUNCTIONS ----------------
	---------------------------------------------------- */
	// Login and Rest posting
	function podsPostFormOne(submitId) {
		console.log("podsPostFormOne function"); // sanity check

		$(submitId).click(function(event){
			// Submit form
			$(submitId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			console.log("Form submitted!"); // sanity check

			// Login form processing
			login_post('employeeLoginTag', 'responseStatus', 'loginEmail', 'loginPass')
		});
	};

	// Sign Up
	function podsPostFormTwo(submitId) {
		console.log("podsPostFormTwo function"); // sanity check

		$(submitId).click(function(event){
			// Submit form
			$(submitId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			console.log("Form submitted!"); // sanity check

			// Sign up form processing
			sign_post('employeeSignupTag', 'responseStatus', 'lastName', 'firstName', 'employeeTel', 'personalTel', 'officeEmail','personalEmail', 'homeAddress', 'signUpPass');
		});
	};

	// Empty, Blank and null form field validation
	function emptyBlankFormFieldValidation(formValues, formValidation) {

		// Check for any empty form field
		for (i = 0; i < formValues.length; i++) {
			var val = formValues[i];
			if (!val || val==="" || val.length < 0 || val == null || val.trim() === '') {
				formValidation = false;
			}
		}
		return formValidation;
	}

	// AJAX POST Processing
	function ajaxPodsProcess (formValidation, formData, responseStatus) {

		// Validation check
		if (formValidation) {
			console.log("Ajax starts...");

			// Start AJAX process
			$.ajax({
				url : "create_post/", 	// the endpoint
				type : "POST", 			// http method
				data : formData, 		// data sent with the post request
				dataType : 'json', 		// expected data back from the server

				// handle a successful response
				success : function(json) {
					// 'loginEmail' is only return for login action from the login page
					if(json['loginEmail']) {

						//Session variables
						var newPage = window.location.href + "dashboard/";
						var now = new Date();
						var mins = 30;
						var expirationTime = 0;

						if (now.getHours() != 0) {
							now = (now.getMinutes() + mins) * now.getHours();
							expirationTime = now;
						} else {
							now = (now.getMinutes() + mins);
							expirationTime = now;
						}

						// Set Session
						sessionStorage.setItem("loginEmail", json['loginEmail']);
						sessionStorage.setItem("expires", expirationTime);
						// Redirect
						window.location.replace(newPage);
					}
					// Show, trigger model and display result message
					$("#statusModalContainer").show();
					$("#statusModalButton").trigger("click");
					$('#' + responseStatus).text(json['result']);

					console.log(json); // log the returned json to the console
					console.log("success"); // another sanity check
				},

				// handle a non-successful response
				error : function(xhr,errmsg,err) {
					$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
						" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
					console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
				}
			});
		} else {
			console.log("empty form");
		}
	}

	// Ajax Sign Up form processing method
	function sign_post(tag, responseStatus, lastName, firstName, employeeTel, personalTel, officeEmail,
	personalEmail, homeAddress, signUpPass) {
		console.log("create post is working!") // sanity check
		var formValidation = true;

		// Get form data
		var formData = {
			employeeSignupTag : $('#' + tag).val(),
			lastName : $('#' + lastName).val(),
			firstName : $('#' + firstName).val(),
			employeeTel : $('#' + employeeTel).val(),
			personalTel : $('#' + personalTel).val(),
			officeEmail : $('#' + officeEmail).val(),
			personalEmail : $('#' + personalEmail).val(),
			homeAddress : $('#' + homeAddress).val(),
			signUpPass : $('#' + signUpPass).val(),
		};

		// Get form values
		var formValues = Object.values(formData);

		// Check for any empty form field
		formValidation = emptyBlankFormFieldValidation(formValues, formValidation);

		// Validate
		if (formValidation) {
			// Process AJAX POST
			ajaxPodsProcess (formValidation, formData, responseStatus);
		}
	};

	// Ajax Login form processing method
	function login_post(tag, responseStatus, loginEmail, loginPass) {

		console.log("Login post is working!") // sanity check
		var formValidation = true;

		// Get form data
		var formData = {
			employeeLoginTag : $('#' + tag).val(),
			loginEmail : $('#' + loginEmail).val(),
			loginPass : $('#' + loginPass).val(),
		};

		// Get form values
		var formValues = Object.values(formData);

		// Check for any empty form field
		formValidation = emptyBlankFormFieldValidation(formValues, formValidation);
		// Validate
		if (formValidation) {
			// Process AJAX POST
			ajaxPodsProcess (formValidation, formData, responseStatus);
		}
	};
});