/**
	Pods Dashboard .js
*/

$(document).ready(function() {
	

	/** Function calls */
	
	// Logout
    logout("#logout");
	
	// Toggle tab
	toggleSidebar("#sidebarCollapse", "#sidebar");
	
	/** Interactive function calls - Key Pages dropdown functions */
    showTabContentAndFocus("#keyLocations", "#setupAndConfigTab", "#setupCollapse", "#locationSetupButton", "#monitoringToolTab");
    showTabContentAndFocus("#keyDevices", "#setupAndConfigTab", "#setupCollapse", "#deviceSetupButton", "#monitoringToolTab");
    showTabContentAndFocus("#keyClusters", "#setupAndConfigTab", "#setupCollapse", "#clusterSetupButton", "#monitoringToolTab");
    showTabContentAndFocus("#keyContents", "#setupAndConfigTab", "#setupCollapse", "#contentSetupButton", "#monitoringToolTab");
    showTabContentAndFocus("#keyClients", "#setupAndConfigTab", "#setupCollapse", "#clientSetupButton", "#monitoringToolTab");
    showTabContentAndFocus("#keyEmployees", "#setupAndConfigTab", "#setupCollapse", "#employeesSetupButton", "#monitoringToolTab");

    // Some specific Setups/Configurations display functions
    setupTabContentAndFormDisplay("#navClientSetup", "#setupAndConfigTab", "#setupCollapse", "#clientSetupCollapse", "#createClientProfileCollapse", "#monitoringToolTab");
    setupTabContentAndFormDisplay("#navContentSetup", "#setupAndConfigTab", "#setupCollapse", "#ContentSetupCollapse", "#createContentsSetupCollapse", "#monitoringToolTab");
    setupTabContentAndFormDisplay("#navChangeRequest", "#setupAndConfigTab", "#setupCollapse", "#changeRequestSetupCollapse", "#createChangeRequestCollapse", "#monitoringToolTab");
    setupTabContentAndFormDisplay("#navContentContracts", "#setupAndConfigTab", "#setupCollapse", "#ContentSetupCollapse", "#createContentContractsCollapse", "#monitoringToolTab");
    showTabElementContent("#navOther", "#setupAndConfigTab", "#monitoringToolTab");

	// Date picker
	//podsDatePicker('#deviceManufacturedYearInput');
    // Setup/Configuration and Monitoring show/hide control
    setupAndMonitoringToolDisplay("#setupAndConfigButton", "#monitoringToolCollapse");
    setupAndMonitoringToolDisplay("#monitoringToolButton", "#setupCollapse");
	
	/** Form Functions */
	// Create Country
	createCountryForm("#podsCreateCountry", 'createCountryTag', 'countryInput', 'continentInput', 'countries');

	// Create City	
	createCityForm("#podsCreateCity", 'createCityTag', 'countryOfCityInput', 'cityNameInput', 'cities');

	// Create Area	
	createAreaForm("#podsCreateArea", 'createAreaTag', 'cityOfAreaInput', 'areaNameInput', 'areas');
	
	// Create Device	
	createDeviceForm("#podsCreateDevice", 'createDeviceTag', 'deviceMacAddressInput', 'deviceStatusInput', 'devices');

	// Create Device Configuration	
	createDeviceConfigForm("#podsCreateDeviceConfig", 'createDeviceConfigTag', 'deviceOfDeviceConfigInput', 'deviceManufacturedYearInput', 'deviceExtraInfoInput', 'none');	
	
	// Create Cluster Types	
	createClusterTypeForm("#podsCreateClusterType", 'createClusterTypeTag', 'clusterTypeInput', 'clusterTypes');
	
	// Create Cluster Setup 	
	createClusterSetupForm("#podsCreateClusterSetup", 'createClusterSetupTag', 'clusterSetupOfAreaInput', 'clusterTypeOfClusterSetupInput', 'clusterExposureInput', 'clusterStatusInput', 'clusterLocationDetailInput', 'clusterSetups');
	
	// Create Cluster Network Configuration 	
	createClusterNetworkConfigForm("#podsCreateClusterNetworkConfig", 'createClusterNetworkConfigTag', 'clusterSetupOfClusterNetConfigInput', 'clusterNetworkProviderInput', 'clusterNetworkPassInput', 'none');
	
	// Create Content Types	
	createContentTypeForm("#podsCreateContentType", 'createContentTypeTag', 'contentTypeInput', 'contentTypes');
	
	// Create Content Setup	
	createContentSetupForm("#podsCreateContentSetup", 'createContentSetupTag', 'contentTypeOfContentSetupInput', 'contentTitleInput', 'isContentNewInput', 'contentContractFeeInput', 'contentContractStartInput', 'contentContractEndInput', 'clientProfileOfContentSetupInput', 'employeeOfContentSetupInput', 'contentDataInput', 'contentContractDataInput', 'contentSetups');
	
	// Create Client Profile
	createClientProfileForm("#podsCreateClientProfile", 'createClientProfileTag', 'clientNameInput', 'clientTelInput', 'clientContactPersonInput', 'clientEmailInput', 'clientAddressInput', 'clientProfiles');

	// Create Active Cluster, Content and Device Setup
	createActiveClusterAndDevicesForm("#podsCreateActiveCAndDevice", 'createActiveClusterAndDevicesTag', 'clusterSetupOfActiveCandDeviceInput', 'deviceOfActiveCandDeviceInput', 'none');
	
	// Create Active Cluster and Content Setup
	createActiveClusterAndContentsForm("#podsCreateActiveCAndContent", 'createActiveClusterAndContentsTag', 'clusterSetupOfActiveCandContentInput', 'contentSetupOfActiveCandContentInput', 'none');
	
	/** Find/Search/fetch method calls */
	// Fetch all list data required onload
	fetchAllRequiredListDataOnLoad('onloadTag');
	
	fetchClusterDetails('#podsSearchClusterDetails', 'findClusterDetailsTag', 'cityOfClusterDetailsInput', 'areaOfClusterDetailsInput', 'clusterSetupOfClusterDetailsInput', 'none');
	
	/** NOTE: NOT RELEVANT AT THE MOMENT
	//Click and fatch list of countries data
	//getListDataOnOnclick('locationSetupButton', 'locationSetupButtonTag', 'countryOfCityInput', 'countriesListCityInputDiv'); 
	*/
	
	/** -----------------LOGOUT FUNCTIONS ----------------
	---------------------------------------------------- */
    // Logout
    function logout(podsLogoutId) {
        $(podsLogoutId).click(function() {
            sessionStorage.clear();
            var newPage = "http://127.0.0.1:8000/";
            window.location.replace(newPage); // Redirect
        });
    }

	
    /********************* INTERACTIVE Functions ***************/
	// Toggle tab
	function toggleSidebar(sidebarCollapse, sidebar) {
		$(sidebarCollapse).on('click', function() {
			$(sidebar).toggleClass('active');
		});
	}
	
    // Setup and Monitoring Tool display function
    function setupAndMonitoringToolDisplay(mainId, controlledId) {
        $(mainId).click(function() {
            var isVisible = $(controlledId).is(":visible");

            if (isVisible) {
                $(controlledId).collapse('hide');
                $(mainId).collapse('show');
                //$(mainId).show();
            } else {
                $(mainId).collapse('show');
                //$(mainId).show();
            }
        });
    }

    // A button for Setup and Monitoring Tool display function
    function setupAndMonitoringToolDisplayFromAnotherButton(clickedButton, mainId, controlledId) {
        $(clickedButton).click(function() {
            var isVisible = $(controlledId).is(":visible");

            if (isVisible) {
                $(controlledId).collapse('hide');
                $(mainId).collapse('show');
                //$(mainId).show();
            } else {
                $(mainId).collapse('show');
                //$(mainId).show();
            }
        });
    }
    // Display 3-level nested contents onclick and check if a top-level div is displayed
    function setupContentAndFormDisplay(clickedButton, sub1, sub2, sub3, checkDisplay) {
        $(clickedButton).click(function() {
            $(sub1).collapse('show');
            $(sub2).collapse('show');
            $(sub3).collapse('show');
            $(checkDisplay).collapse('hide');
        });
    }
    // Display 3-level nested contents of a "Tab" onclick and check if a top-level "Tab" is displayed
    function setupTabContentAndFormDisplay(clickedButton, tab, sub1, sub2, sub3, checkDisplay) {
        $(clickedButton).click(function() {
            $(tab).tab('show');
            $(sub1).collapse('show');
            $(sub2).collapse('show');
            $(sub3).collapse('show');
            $(checkDisplay).tab('hide');
        });
    }
    // Show/Display an element onclick
    function showElementContent(clickedButton, controlled) {
        $(clickedButton).click(function() {
            $(controlled).collapse('show');
        });
    }
    // Show/Display a Tab and hide the other onclick
    function showTabElementContent(clickedButton, tab, controlled, checkDisplay) {
        $(clickedButton).click(function() {
            $(tab).tab('show');
            $(checkDisplay).tab('hide');
        });
    }
    //Show content and focus
    function showContentAndFocus(clickedButton, controlled, focusElement, checkDisplay) {
        $(clickedButton).click(function() {
            $(controlled).collapse('show');
            $(focusElement).focus();
            $(checkDisplay).collapse('hide');
        });
    }
    //Show tab content and focus
    function showTabContentAndFocus(clickedButton, tab, controlled, focusElement, checkDisplay) {
        $(clickedButton).click(function() {
            $(tab).tab('show');
            $(controlled).collapse('show');
            $(focusElement).focus();
            $(checkDisplay).tab('hide');
        });
    }
	
	/* Date picker
	function podsDatePicker(inputFieldId) {
		//$( document ).ready(function() {
			$(inputFieldId).datepicker({ 
				format: 'yyyy-mm-dd'
			});
			$(inputFieldId).on("change", function () {
				var fromdate = $(this).val();
				alert(fromdate);
			});
		//}); 
	
	}
	*/
	/*************** INTERACTIVE Functions depending on AJAX *******
	----------------------------------------------------*/
	// Generic fetch all required list data, save in seperate sessions, update all respective 
	// Select elements onload.
	function fetchAllRequiredListDataOnLoad(ajaxRequestTag) {
		console.log("fetchAllRequiredListDataOnLoad function"); // sanity check

		// GET request data
		var formData = {
			ajaxRequestTag : ajaxRequestTag,	
		};
		
		console.log("Start AJAX processing..."); // sanity check
		// Start AJAX process
		$.ajax({
			url : "get_data_request/", 	// the endpoint
			type : "GET", 				// http method
			data : formData, 			// data sent with the post request
			dataType : 'json', 			// expected data back from the server

			// handle a successful response
			success : function(json) {
				console.log("fetch all data from Onload Action"); // Sanity check

				Object.keys(json).forEach(function(key) {
					console.log("For : " + key); // sanity check

					// A new JSON object with list values
					var nJson = json[key];
					
					// Store each list data in a unique session 
					storeResponseToSession (key, nJson);
				});
				
				// Read sessions data
				var employeesSessionData = sessionStorage.getItem('employees');				
				var countiesSessionData = sessionStorage.getItem('countries');				
				var citiesSessionData = sessionStorage.getItem('cities');					
				var areasSessionData = sessionStorage.getItem('areas');						
				var devicesSessionData = sessionStorage.getItem('devices');						
				var clusterTypesSessionData = sessionStorage.getItem('clusterTypes');
				var clusterSetupsSessionData = sessionStorage.getItem('clusterSetups');
				var contentTypesSessionData = sessionStorage.getItem('contentTypes');	
				var clientProfilesSessionData = sessionStorage.getItem('clientProfiles');	
				var contentSetupsSessionData = sessionStorage.getItem('contentSetups');	
				
				// Convert session data to JSON	
				var employeesJSONData = JSON.parse(employeesSessionData);	
				var countriesJSONData = JSON.parse(countiesSessionData);	
				var citiesJSONData = JSON.parse(citiesSessionData);	
				var areasJSONData = JSON.parse(areasSessionData);	
				var devicesJSONData = JSON.parse(devicesSessionData);	
				var clusterTypesJSONData = JSON.parse(clusterTypesSessionData);	
				var clusterSetupsJSONData = JSON.parse(clusterSetupsSessionData);	
				var contentTypesJSONData = JSON.parse(contentTypesSessionData);	
				var clientProfilesJSONData = JSON.parse(clientProfilesSessionData);	
				var contentSetupsJSONData = JSON.parse(contentSetupsSessionData);	
				
				console.log("Latest : " + clientProfilesJSONData);	// Sanity check

				/* List all Select Elements that requires in it's form below: */
				returnSelectElementAndOptionInput (employeesJSONData, 'employeeOfContentSetupInput', 'Employee Rep.');
				
				returnSelectElementAndOptionInput (countriesJSONData, 'countryOfCityInput', 'Country');
				
				returnSelectElementAndOptionInput (citiesJSONData, 'cityOfAreaInput', 'City');
				returnSelectElementAndOptionInput (citiesJSONData, 'cityOfClusterDetailsInput', 'City');
				
				returnSelectElementAndOptionInput (areasJSONData, 'clusterSetupOfAreaInput', 'Area');		
				returnSelectElementAndOptionInput (areasJSONData, 'clusterSetupOfAreaInput', 'Area');		
				returnSelectElementAndOptionInput (areasJSONData, 'areaOfClusterDetailsInput', 'Area');		
				
				returnSelectElementAndOptionInput (devicesJSONData, 'deviceOfDeviceConfigInput', 'Device');
				returnSelectElementAndOptionInput (devicesJSONData, 'deviceOfActiveCandDeviceInput', 'Device');
				
				returnSelectElementAndOptionInput (clusterTypesJSONData, 'clusterTypeOfClusterSetupInput', 'Cluster Type');
				
				returnSelectElementAndOptionInput (contentTypesJSONData, 'contentTypeOfContentSetupInput', 'Content Type');
				
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterNetConfigInput', 'Cluster Setup');
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterWeatherConfigInput', 'Cluster Setup');				
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfActiveCandDeviceInput', 'Cluster Setup');
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfActiveCandContentInput', 'Cluster Setup');
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterDetailsInput', 'Cluster Setup');
				
				returnSelectElementAndOptionInput (contentSetupsJSONData, 'contentSetupOfActiveCandContentInput', 'Content Setup');
				
				returnSelectElementAndOptionInput (clientProfilesJSONData, 'clientProfileOfContentSetupInput', 'Client Profile');
				/**/
				console.log("*** fetchAllRequiredListDataOnLoad END ***"); // another sanity check
			},					

			// handle a non-successful response
			error : function(xhr,errmsg,err) {
				$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+ errmsg + " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
				console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
				}
		});	
		console.log("*** fetchAllRequiredListDataOnLoad END ***"); // another sanity check	
	}
	
	
	// Proccess AJAX JSON data returned or saved Session data, display it as an input option under <select> element.
	function returnSelectElementAndOptionInput (json, selectInputElementId, defaultSelectName) {
		console.log("returnSelectElementAndOptionInput function"); // sanity check

		var strValue ="<option value=\"NO DATA\" selected>Select " + defaultSelectName + "</option>";
		
		// Fetch/Extra data from returned JSON data
		Object.keys(json).forEach(function(key) {
						
			strValue = strValue.concat("<option value='"+ (json[key]) +"'>"+ json[key] +"</option>");
			console.table('Key : ' + key + ', Value : ' + json[key])
		});
					
		//strValue = "<select class='form-control selectpicker' id='" + selectInputElementId + "' data-live-search='true' required>" + strValue + "</select>";
		
		//var currentElementValue = document.getElementById(selectInputElementId).innerHTML;
		
		// Update input div inner HTML
		//document.getElementById(selectInputElementId).innerHTML = currentElementValue.concat(strValue);
		document.getElementById(selectInputElementId).innerHTML = strValue;

		$('#' + selectInputElementId).selectpicker('refresh');		// Refresh element (VERY IMPORTANT)!

		console.log("*** returnSelectElementAndOptionInput END ***"); // another sanity check	
	}
	
	
	/** --------- SESSION FUNCTIONS ----------------
	---------------------------------------------------- */
	
	// Store JSON data format received from AJAX response.
	function storeResponseToSession (sessionName, responseJSONData) {
		console.log("storeResponseToSession function"); // sanity check

		var JSONData = "{";										
		//var x = json[formData.sessionName];
					
		// Fetch/Extra data from returned JSON data
		Object.keys(responseJSONData).forEach(function(key) {
			var currentVal = "\"" + key + "\"" + ":" + "\"" + responseJSONData[key] + "\"," ;
				
			JSONData = JSONData + currentVal;
			console.table(JSONData);
		});
					
		JSONData = JSONData.slice(0, (JSONData.length - 1)) + "}";
		console.log("Session Data: " + JSONData);
		
		// Replace old session with a new session
		sessionStorage.setItem(sessionName, JSONData);	
		
		console.log("*** storeResponseToSession END ***"); // another sanity check			
	}

	// AJAX Login POST request Processing
	function ajaxPodsProcess (formValidation, formData, responseStatus) {

		// Validation check
		if (formValidation) {
			console.log("Ajax starts...");

			// Start AJAX process
			$.ajax({
				url : "setup_post/", 	// the endpoint
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

	// AJAX Setup or any configuration create POST request Process
	function ajaxSetupProcessing (formValidation, formData) {
		console.log("ajaxSetupProcessing function...");

		var returnedData 
		// Validation check
		if (formValidation) {

			// Start AJAX process
			$.ajax({
				url : "setup_post/", 	// the endpoint
				type : "POST", 			// http method
				async: false,			// asynchronously run AJAX (i.e. waits for 
										// AJAX before proceeding). DEPRECATED option
				data : formData, 		// data sent with the post request
				dataType : 'json', 		// expected data back from the server

				// handle a successful response
				success : function(json) {
					console.log("Session response content: " + json[formData.sessionName]);
					
					if (json[formData.sessionName]) {
						storeResponseToSession (formData.sessionName, json[formData.sessionName]);
					}
					// Show, trigger model and display the result  message of AJAX response
					// from server. i.e. >> json['result'] <<
					displayConfirmationMessage(json['result']);		
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
		
		console.log("*** ajaxSetupProcessing END ***"); // another sanity check	
	}		
	
	// AJAX Get request Process
	function ajaxGetRequestProcessing (formValidation, formData) {
		console.log("ajaxGetRequestProcessing function...");

		var returnedData 
		// Validation check
		if (formValidation) {

			// Start AJAX process
			$.ajax({
				url : "get_data_request/", 	// the endpoint
				type : "POST", 			// http method
				async: false,			// asynchronously run AJAX (i.e. waits for 
										// AJAX before proceeding). DEPRECATED option
				data : formData, 		// data sent with the post request
				dataType : 'json', 		// expected data back from the server

				// handle a successful response
				success : function(json) {
					console.log("Session response content: " + json[formData.sessionName]);
					
					if (json[formData.sessionName]) {
						storeResponseToSession (formData.sessionName, json[formData.sessionName]);
					}
					
					Object.keys(json).forEach(function(key) {
						console.log("--For : " + key); // sanity check
					
						// A new JSON object with list values
						var nJson = json[key];
						strValue = "<tr>";
						Object.keys(nJson).forEach(function(nkey) {
							console.log("nkey : " + nJson[nkey]); // sanity check
							
							var nnJson = nJson[nkey];							
							Object.keys(nnJson).forEach(function(nnkey) {
								console.log("nnkey : " + nnJson[nnkey]); // sanity check
								
								if(nnkey == 'ActiveClusterAndContent__content_setup__content_data') {
									strValue = strValue.concat("<td><img class=\"img-thumbnail\" src='" + nnJson[nnkey] + "'></td>");
								} else {
									strValue = strValue.concat("<td>" + nnJson[nnkey] + "</td>");
								}								
							});
							strValue = strValue.concat("</tr>");
					
						});

						//console.log("Final result: ", strValue);
							
					
						if(key == 'Cluster Detail') {
								document.getElementById("clusterDetailsTable").innerHTML = strValue;	
							} else if (key == 'Devices') {
								document.getElementById("deviceDetailsTable").innerHTML = strValue;								
							} else if (key == 'Contents') {
								document.getElementById("contentDetailsTable").innerHTML = strValue;								
						}
					});		
					$("#clusterDetailResultsDiv").show();
					// Show, trigger model and display the result  message of AJAX response
					// from server. i.e. >> json['result'] <<
					//displayConfirmationMessage(json['content_title']);		
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
		
		console.log("*** ajaxGetRequestProcessing END ***"); // another sanity check	
	}	

/*	
	// AJAX Setup POST request with FILE CONTENT Process
	function ajaxWithFileSetupProcessing (formValidation, formData) {
		console.log("ajaxWithFileSetupProcessing function...");

		var returnedData 
		// Validation check
		if (formValidation) {
			//var formData = jQuery('#createContentSetupForm').serializeArray();
			//var data = new FormData($('#createContentSetupForm').get(0));
			console.log(formData)
			
			// Start AJAX process
			$.ajax({
				url : "setup_post/", 	// the endpoint
				type : "POST", 			// http method
				async: false,			// asynchronously run AJAX (i.e. waits for 
										// AJAX before proceeding). DEPRECATED option
				data : formData, 		// data sent with the post request
				//dataType : 'json', 		// expected data back from the server
				cache: false,
                contentType: false,
                processData: false,
				// handle a successful response
				success : function(json) {
					console.log("Session response content: " + json[formData.sessionName]);
					
					if (json[formData.sessionName]) {
						storeResponseToSession (formData.sessionName, json[formData.sessionName]);
					}
					// Show, trigger model and display the result  message of AJAX response
					// from server. i.e. >> json['result'] <<
					displayConfirmationMessage(json['result']);		
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
		
		console.log("*** ajaxWithFileSetupProcessing END ***"); // another sanity check	
	}	
	*/
	
	/** --------- FORM FILED VALIDATION FUNCTIONS ----------------
	---------------------------------------------------- */
	
	// Empty, Blank and null form field validation
	function emptyBlankFormFieldValidation(formValues, formValidation) {
		console.log("emptyBlankFormFieldValidation function...");
		
		// Check for any empty form field
		for (i = 0; i < formValues.length; i++) {
			var val = formValues[i];
			if (!val || val==="" || val.length < 0 || val == null || val.trim() === ''|| val === 'NO DATA') {
				formValidation = false;
			}
		}
		
		console.log("*** emptyBlankFormFieldValidation END ***"); // another sanity check	
		return formValidation;
	}
	
			
	/** ---- RESPONSE RESULT MESSAGE DISPLAY -----------
	---------------------------------------------------- */
	// Show, trigger model and display result message
	function displayConfirmationMessage(JSONResult) {		
		console.log("displayConfirmationMessage function...");

		$("#statusModalContainer").show();
		$("#statusModalButton").trigger("click");
		$("#responseStatus").text(JSONResult);
		
		console.log("*** displayConfirmationMessage END ***"); // another sanity check	
	}

	/** -- FORM SETUP CAPTURING, VALIDATION AND PROCESSING FUNCTIONS ------
	----------------------------------------------------------------------- */	
	
	// Create/Setup/Configuration form data capturing, validation and processing
	function formDataCapturingValidationAndProcessing(formData) {
		console.log("formDataCapturingValidationAndProcessing function") // sanity check
		var formValidation = true;
				
		// Get form values
		var formValues = Object.values(formData);
		
		// Check for any empty form field
		formValidation = emptyBlankFormFieldValidation(formValues, formValidation);
		console.log("Validation outcome: " + formValidation);
		
		// Validate
		if (formValidation) {
			console.log("Fields validation Pass");

			// AJAX setup POST request process
			ajaxSetupProcessing (formValidation, formData);
		}
		
		console.log("*** formDataCapturingValidationAndProcessing END ***"); // another sanity check			
		return formValidation;
	};
	
	// Fetch/Search/Get request form data capturing, validation and processing
	function getRequestFormDataCapturingValidationAndProcessing(formData) {
		console.log("getRequestFormDataCapturingValidationAndProcessing function") // sanity check
		var formValidation = true;
				
		// Get form values
		var formValues = Object.values(formData);
		
		// Check for any empty form field
		formValidation = emptyBlankFormFieldValidation(formValues, formValidation);
		console.log("Validation outcome: " + formValidation);
		
		// Validate
		if (formValidation) {
			console.log("Fields validation Pass");

			// AJAX setup POST request process
			ajaxGetRequestProcessing (formValidation, formData);
		}
		
		console.log("*** getRequestFormDataCapturingValidationAndProcessing END ***"); // another sanity check			
		return formValidation;
	};
	
	/** ------------- Create Country Form Processing ---------- */	
	// Create Country POST initiation
	function createCountryForm(submitButtonId, ajaxRequestTag, countryInput, continentInput, sessionName) {

		$(submitButtonId).click(function(event){			
			console.log("createCountryForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				countryInput : $('#' + countryInput).val(),
				continentInput : $('#' + continentInput).val(),			
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Country form processing..."); // sanity check
			console.log(formData); // sanity check
			
			// Create a Country from capturing, validation,
			// AJAX request processing and storing response data in session
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {
				// Read  >>countries<< session data
				var countriesSessionData = sessionStorage.getItem('countries');						
				// Convert session data to JSON	
				var countriesJSONData = JSON.parse(countriesSessionData);	
					
				console.log("Latest : " + countriesJSONData);	// Sanity check

				/* List all Select Elements that requires COUNTRY in it's form below: */
				returnSelectElementAndOptionInput (countriesJSONData, 'countryOfCityInput', 'Country');				
			}	
					
			console.log("*** createCountryForm END ***"); // another sanity check	
		});
	};
	
	/** ------------- Create City Form Processing ---------- */	
	// Create City POST initiation
	function createCityForm(submitButtonId, ajaxRequestTag, countryOfCityInput, cityNameInput, sessionName) {


		$(submitButtonId).click(function(event){
			console.log("createCityForm function"); // sanity check
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				countryOfCityInput : $('#' + countryOfCityInput).val(),
				cityNameInput : $('#' + cityNameInput).val(),			
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create City form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a City form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>countries<< session data
				var citiesSessionData = sessionStorage.getItem('cities');						
				// Convert session data to JSON	
				var citiesJSONData = JSON.parse(citiesSessionData);	
					
				console.log("Latest : " + citiesJSONData);	// Sanity check

				/* List all Select Elements that requires COUNTRY in it's form below: */
				returnSelectElementAndOptionInput (citiesJSONData, 'cityOfAreaInput', 'City');
				returnSelectElementAndOptionInput (citiesJSONData, 'cityOfClusterDetailsInput', 'City');
			}		
			
			console.log("*** createCityForm END ***"); // another sanity check	
		});
	};
		
	/** ------------- Create Area Form Processing ---------- */	
	// Create Area POST initiation
	function createAreaForm(submitButtonId, ajaxRequestTag, cityOfAreaInput, areaNameInput, sessionName) {


		$(submitButtonId).click(function(event){
			console.log("createAreaForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				cityOfAreaInput : $('#' + cityOfAreaInput).val(),
				areaNameInput : $('#' + areaNameInput).val(),			
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Area form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Area form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>Areas<< session data
				var areasSessionData = sessionStorage.getItem('areas');						
				// Convert session data to JSON	
				var areasJSONData = JSON.parse(areasSessionData);	
					
				console.log("Latest : " + areasJSONData);	// Sanity check

				/* List all Select Elements that requires AREA in it's form below: */
				returnSelectElementAndOptionInput (areasJSONData, 'clusterSetupOfAreaInput', 'Area');
				returnSelectElementAndOptionInput (areasJSONData, 'areaOfClusterDetailsInput', 'Area');	
			}
			
			console.log("*** createAreaForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Device Form Processing ---------- */	
	// Create Device POST initiation
	function createDeviceForm(submitButtonId, ajaxRequestTag, deviceMacAddressInput, deviceStatusInput, sessionName) {


		$(submitButtonId).click(function(event){
			console.log("createDeviceForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				deviceMacAddressInput : $('#' + deviceMacAddressInput).val(),
				deviceStatusInput : $('#' + deviceStatusInput).val(),			
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Device form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Device form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>Devices<< session data
				var devicesSessionData = sessionStorage.getItem('devices');						
				// Convert session data to JSON	
				var devicesJSONData = JSON.parse(devicesSessionData);	
					
				console.log("Latest : " + devicesJSONData);	// Sanity check

				/* List all Select Elements that requires DEVICE in it's form below: */
				returnSelectElementAndOptionInput (devicesJSONData, 'deviceOfDeviceConfigInput', 'Device');
				returnSelectElementAndOptionInput (devicesJSONData, 'deviceOfActiveCandDeviceInput', 'Device');
			}
			
			console.log("*** createDeviceForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Device Configuration Form Processing ---------- */	
	// Create Device POST initiation
	function createDeviceConfigForm(submitButtonId, ajaxRequestTag, deviceOfDeviceConfigInput, deviceManufacturedYearInput, deviceExtraInfoInput, sessionName) {


		$(submitButtonId).click(function(event){
			console.log("createDeviceConfigForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				deviceOfDeviceConfigInput : $('#' + deviceOfDeviceConfigInput).val(),
				deviceManufacturedYearInput : $('#' + deviceManufacturedYearInput).val(),			
				deviceExtraInfoInput : $('#' + deviceExtraInfoInput).val(),			
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Device Configuration form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Device Configuration form processing
			formDataCapturingValidationAndProcessing(formData);
			//console.log("======= Form validation ======: " + formValidation);
			
			console.log("*** createDeviceConfigForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Cluster Type Form Processing ---------- */	
	// Create Cluster type POST initiation
	function createClusterTypeForm(submitButtonId, ajaxRequestTag, clusterTypeInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createClusterTypeForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clusterTypeInput : $('#' + clusterTypeInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Cluster Type form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Cluster Type form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>Cluster Types<< session data
				var clusterTypesSessionData = sessionStorage.getItem('clusterTypes');						
				// Convert session data to JSON	
				var clusterTypesJSONData = JSON.parse(clusterTypesSessionData);	
					
				console.log("Latest : " + clusterTypesJSONData);	// Sanity check

				/* List all Select Elements that requires CLUSTER TYPES in it's form below: */
				returnSelectElementAndOptionInput (clusterTypesJSONData, 'clusterTypeOfClusterSetupInput', 'Cluster Type');
			}
			
			console.log("*** createClusterTypeForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Cluster Setup Form Processing ---------- */	
	// Create Cluster setup POST initiation clusterSetupOfAreaInput
	function createClusterSetupForm(submitButtonId, ajaxRequestTag, clusterSetupOfAreaInput, clusterTypeOfClusterSetupInput,  clusterExposureInput, clusterStatusInput, clusterLocationDetailInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createClusterSetupForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clusterSetupOfAreaInput : $('#' + clusterSetupOfAreaInput).val(),
				clusterTypeOfClusterSetupInput : $('#' + clusterTypeOfClusterSetupInput).val(),
				clusterExposureInput : $('#' + clusterExposureInput).val(),
				clusterStatusInput : $('#' + clusterStatusInput).val(),
				clusterLocationDetailInput : $('#' + clusterLocationDetailInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Cluster Setup form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Cluster Setup form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
						
			if (formValidation) {			
				// Read >>Cluster Setups<< session data
				var clusterSetupsSessionData = sessionStorage.getItem('clusterSetups');						
				// Convert session data to JSON	
				var clusterSetupsJSONData = JSON.parse(clusterSetupsSessionData);	
					
				console.log("Latest : " + clusterSetupsJSONData);	// Sanity check

				/* List all Select Elements that requires CLUSTER TYPES in it's form below: */
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterNetConfigInput', 'Cluster Setup');returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterWeatherConfigInput', 'Cluster Setup');
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterDetailsInput', 'Cluster Setup');
			} 
			
			console.log("*** createClusterSetupForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Cluster Network Configuration Form Processing ---------- */	
	// Create Cluster Network Configuration POST initiation
	function createClusterNetworkConfigForm(submitButtonId, ajaxRequestTag, clusterSetupOfClusterNetConfigInput, clusterNetworkProviderInput,  clusterNetworkPassInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createClusterNetworkConfigForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clusterSetupOfClusterNetConfigInput : $('#' + clusterSetupOfClusterNetConfigInput).val(),
				clusterNetworkProviderInput : $('#' + clusterNetworkProviderInput).val(),
				clusterNetworkPassInput : $('#' + clusterNetworkPassInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Cluster Network Configuration form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Cluster Network Configuration form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			/*
			if (formValidation) {			
				// Read >>Cluster Setups<< session data
				var clusterSetupsSessionData = sessionStorage.getItem('clusterSetups');						
				// Convert session data to JSON	
				var clusterSetupsJSONData = JSON.parse(clusterSetupsSessionData);	
					
				console.log("Latest : " + clusterSetupsJSONData);	// Sanity check

				/* List all Select Elements that requires CLUSTER TYPES in it's form below: 
				returnSelectElementAndOptionInput (clusterSetupsJSONData, 'clusterSetupOfClusterNetConfigInput', 'clusterSetupListClusterNetConfigDiv');
			} */
			
			console.log("*** createClusterNetworkConfigForm END ***"); // another sanity check
		});
	};
	
	/** ------------- Create Content Type Form Processing ---------- */	
	// Create Content type POST initiation
	function createContentTypeForm(submitButtonId, ajaxRequestTag, contentTypeInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createContentTypeForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				contentTypeInput : $('#' + contentTypeInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Content Type form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Content Type form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>Content Types<< session data
				var contentTypesSessionData = sessionStorage.getItem('contentTypes');						
				// Convert session data to JSON	
				var contentTypesJSONData = JSON.parse(contentTypesSessionData);	
					
				console.log("Latest : " + contentTypesJSONData);	// Sanity check

				/* List all Select Elements that requires CONTENT TYPES in it's form below:*/
				returnSelectElementAndOptionInput (contentTypesJSONData, 'contentTypeOfContentSetupInput', 'Content Type');
			}
			
			console.log("*** createContentTypeForm END ***"); // another sanity check
		});
	};

	/** ------------- Create Client Profile Form Processing ---------- */	
	// Create Client Profile POST initiation
	function createClientProfileForm(submitButtonId, ajaxRequestTag, clientNameInput, clientTelInput, clientContactPersonInput, clientEmailInput, clientAddressInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createClientProfileForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clientNameInput : $('#' + clientNameInput).val(),
				clientTelInput : $('#' + clientTelInput).val(),
				clientContactPersonInput : $('#' + clientContactPersonInput).val(),
				clientEmailInput : $('#' + clientEmailInput).val(),
				clientAddressInput : $('#' + clientAddressInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Client Profile form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create a Client Profile form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			if (formValidation) {			
				// Read >>Client Profiles<< session data
				var clientProfilesSessionData = sessionStorage.getItem('clientProfiles');						
				// Convert session data to JSON	
				var clientProfilesJSONData = JSON.parse(clientProfilesSessionData);	
					
				console.log("Latest : " + clientProfilesJSONData);	// Sanity check

				/* List all Select Elements that requires CLIENT PROFILE in it's form below: */
				returnSelectElementAndOptionInput (clientProfilesJSONData, 'clientProfileOfContentSetupInput', 'Client Profile');
			}
			
			console.log("*** createClientProfileForm END ***"); // another sanity check
		});
	};

	
	/** ------------- Create Content Setup Form Processing ---------- */	
	// Create Content Setup POST initiation
	function createContentSetupForm(submitButtonId, ajaxRequestTag, contentTypeOfContentSetupInput, contentTitleInput, isContentNewInput, contentContractFeeInput, contentContractStartInput, contentContractEndInput, clientProfileOfContentSetupInput, employeeOfContentSetupInput, contentDataInput, contentContractDataInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createContentSetupForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
			
			// Get form data - CAN BE REFACTORED BETTER
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				contentTypeOfContentSetupInput : document.querySelector('#' + contentTypeOfContentSetupInput).value,
				clientProfileOfContentSetupInput : document.querySelector('#' + clientProfileOfContentSetupInput).value,
				contentTitleInput : document.querySelector('#' + contentTitleInput).value,
				isContentNewInput : document.querySelector('#' + isContentNewInput).value,
				contentContractFeeInput : document.querySelector('#' + contentContractFeeInput).value,
				contentContractStartInput : document.querySelector('#' + contentContractStartInput).value,
				contentContractEndInput : document.querySelector('#' + contentContractEndInput).value,
				employeeOfContentSetupInput : document.querySelector('#' + employeeOfContentSetupInput).value,
				contentDataInput : $('#' + contentDataInput).val(), // Just file path 
				contentContractDataInput : $('#' + contentContractDataInput).val(), // Just file path
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Content setup form processing..."); // sanity check
			
			// Create a Content Setup form processing			
			var formValidation = true;
				
			// Get form values
			var formValues = Object.values(formData);
			
			// Check for any empty form field
			formValidation = emptyBlankFormFieldValidation(formValues, formValidation);
			console.log("Validation outcome: " + formValidation);

			console.log(formData); // sanity check
	
			// Validate
			if (formValidation) {
				console.log("Fields validation Pass");

				// AJAX setup POST request process
				//ajaxWithFileSetupProcessing (formValidation, formData);
							
				var data = new FormData();
				var request = new XMLHttpRequest();
				
				data.append('ajaxRequestTag', formData.ajaxRequestTag);
				data.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);
				data.append(contentTypeOfContentSetupInput, formData.contentTypeOfContentSetupInput);
				data.append(contentTitleInput, formData.contentTitleInput);
				data.append(isContentNewInput, formData.isContentNewInput);
				data.append(contentContractFeeInput, formData.contentContractFeeInput);
				data.append(contentContractStartInput, formData.contentContractStartInput);
				data.append(contentContractEndInput, formData.contentContractEndInput);
				data.append(clientProfileOfContentSetupInput, formData.clientProfileOfContentSetupInput);
				data.append(employeeOfContentSetupInput, formData.employeeOfContentSetupInput);
				
				data.append(contentDataInput, document.querySelector('#' + contentDataInput).files[0]); // File content
				data.append(contentContractDataInput, document.querySelector('#' + contentContractDataInput).files[0]); // File content
				data.append('sessionName', formData.sessionName);
				data.append('loginEmail', loginEmail);
				
				console.log(data);
				
				// AJAX request finished and response listener
				request.addEventListener('load', function(e) {
					// request.response will hold the response from the server
					if(request.response.error == 1) {
						console.log(request.response);
					}
					else if(request.response.error == 0) {
						alert('File uploaded successfully');
					}
					var response = request.response;
					
					if (response[formData.sessionName]) {
						// Save data to session
						storeResponseToSession(formData.sessionName, response[formData.sessionName]);
					}
					// Read >>Content Setups<< session data
					var contentSetupsSessionData = sessionStorage.getItem('contentSetups');						
					// Convert session data to JSON	
					var contentSetupsJSONData = JSON.parse(contentSetupsSessionData);	
					
					console.log("Latest : " + contentSetupsJSONData);	// Sanity check
					/* List all Select Elements that requires CONTENT TYPES in it's form below: */
					returnSelectElementAndOptionInput (contentSetupsJSONData, 'contentSetupOfActiveCandContentInput', 'Content Setup');

					// Display response result message
					displayConfirmationMessage(response['result']);
					
					console.log("response data");
					console.log(response);
				});

				// Upload progress on request.upload
				request.upload.addEventListener('progress', function(e) {
					var percent_complete = (e.loaded / e.total)*100;
					
					// Percentage of upload completed
					console.log("Progress Status: " + percent_complete);
				});
								
				// If server is sending a JSON response then set JSON response type
				request.responseType = 'json';

				// Send POST request to the server side script
				request.open('POST', 'setup_post/'); 
				request.send(data);
				
			}			
			
			console.log("*** createContentSetupForm END ***"); // another sanity check
		});
	};		

	
	/** ------ Create Active Cluster and Device Setup Form Processing ------ */	
	function createActiveClusterAndDevicesForm(submitButtonId, ajaxRequestTag, clusterSetupOfActiveCandDeviceInput,  deviceOfActiveCandDeviceInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createActiveClusterAndDevicesForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clusterSetupOfActiveCandDeviceInput : $('#' + clusterSetupOfActiveCandDeviceInput).val(),
				deviceOfActiveCandDeviceInput : $('#' + deviceOfActiveCandDeviceInput).val(),		
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Active Cluster and Devices form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create an Active Cluster, Content and Devices form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			console.log("*** createActiveClusterAndDevicesForm END ***"); // another sanity check
		});
	};

	/** ------ Create Active Clusters and Contents Setup Form Processing ------ */	
	function createActiveClusterAndContentsForm(submitButtonId, ajaxRequestTag, clusterSetupOfActiveCandContentInput, contentSetupOfActiveCandContentInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("createActiveClusterAndContentsForm function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				clusterSetupOfActiveCandContentInput : $('#' + clusterSetupOfActiveCandContentInput).val(),
				contentSetupOfActiveCandContentInput : $('#' + contentSetupOfActiveCandContentInput).val(),
				loginEmail : loginEmail, // 	
			};
			
			console.log("Create Active Cluster and Content form processing..."); // sanity check
			console.log(formData); // sanity check

			// Create an Active Cluster and Content form processing
			var formValidation = formDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			console.log("*** createActiveClusterAndContentsForm END ***"); // another sanity check
		});
	};

	
	/***-----------------+++++++++ GET METHODS +++++++--------------- ***/
	/** ------------- Fetch a Cluster Details Form Processing ---------- */		
	function fetchClusterDetails(submitButtonId, ajaxRequestTag, cityOfClusterDetailsInput, areaOfClusterDetailsInput, clusterSetupOfClusterDetailsInput, sessionName) {

		$(submitButtonId).click(function(event){
			console.log("fetchClusterDetails function"); // sanity check
			
			// Submit form
			$(submitButtonId).submit();

			event.preventDefault();
			event.stopImmediatePropagation();

			// Get logged in username/email
			var loginEmail = sessionStorage.getItem('loginEmail');
		
			// Get form data
			var formData = {
				ajaxRequestTag : ajaxRequestTag,
				sessionName: sessionName,
				cityOfClusterDetailsInput : $('#' + cityOfClusterDetailsInput).val(),
				areaOfClusterDetailsInput : $('#' + areaOfClusterDetailsInput).val(),
				clusterSetupOfClusterDetailsInput : $('#' + clusterSetupOfClusterDetailsInput).val(),		
				loginEmail : loginEmail, // 	
			};
			
			console.log("Fetch a Cluster Details form processing..."); // sanity check
			console.log(formData); // sanity check

			// Fetch a Cluster Details orm processing
			var formValidation = getRequestFormDataCapturingValidationAndProcessing(formData);
			console.log("======= Form validation ======: " + formValidation);
			
			console.log("*** fetchClusterDetailss END ***"); // another sanity check
		});
	};
	
});