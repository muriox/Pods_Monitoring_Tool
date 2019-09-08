from django.shortcuts import render
from django.db.models import Q
import datetime
from django.http import HttpResponse
from .models import Test, EmployeesProfile, StaffLogin, Countries, Cities, Areas, Devices, DevicesConfiguration, \
    ClusterTypes, ClustersSetup, ClustersNetworkConfiguration, ContentTypes, ContentsSetupDataContract, \
    ClientsProfile, ActiveClustersAndDevices, ActiveClustersAndContents
from .forms import ContentForm
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json
import uuid


def home(request):
    print('*** Home page ****')
    return render(request, 'pages/index.html')
    #return HttpResponse('<b>Home Page</b>')


def dashboard(request):
    print('*** DashBoard ****')
    return render(request, 'pages/dashboard.html')


def roll(request):
    print('*** roll test ****')

    # Convert UUID value to String without (-) dashes
    # country_data = list(Countries.objects.filter(country_name='TOGO').values('country_id'))
    # country_id = uuid.UUID(str(country_data[0].get('country_id'))).hex
    #
    # print(country_data)
    # print(country_id)
    # val = get_devices_configuration(request, "")
    # print('val')
    # print(val)

    # area_data = Areas.objects.filter(area_name='LEWISHAM').values('area_id')
    # print("Area check pass")
    # print(area_data)
    #
    # cluster_type_data = ClusterTypes.objects.filter(cluster_location_type='HIGHWAY').values('cluster_type_id')
    # print("Cluster Type check pass")
    # print(cluster_type_data)
    #
    # # Convert >> area_id <<  UUID value to String without (-) dashes
    # area_id = uuid.UUID(str(area_data[0].get('area_id'))).hex
    # print("area_id: " + area_id)
    #
    # # Convert >> cluster_type_id <<  UUID value to String without (-) dashes
    # cluster_type_id = uuid.UUID(str(cluster_type_data[0].get('cluster_type_id'))).hex
    # print("cluster_type_id: " + cluster_type_id)
    #
    # # Check if Device Configuration exist
    # cluster_setup_check = ClustersSetup.objects.filter(area=area_id, cluster_type=cluster_type_id)
    #
    # # If Device Configuration record not found
    # if not cluster_setup_check:
    #     print("Cluster Setup doesn't exist")
    #     print(cluster_setup_check)

    # c_data = Cities.objects.get(city_name='LONDON')
    # a_data = Cities.objects.get(city_name='LONDON').areas.all().values()
    # data = Areas.objects.all().values()
    # print(a_data)

    # area_data = Areas.objects.filter(area_name=area_name).values('area_id')
    # print("Area check pass")
    # print(area_data)
    # cluster_setup_data = ClustersSetup.objects.filter(cluster_location_detail='GREENWICH TRAIN STATION') \
    #     .values('cluster_setup_id')
    # last_content_data = Test.objects.last()
    # data = last_content_data.content_data
    # print(last_content_data)

    # data = ActiveClustersAndDevices.objects.values('content_setup').count()
    # data = active_cluster_content_limit_check = ActiveClustersAndContents.objects\
    #         .filter(cluster_setup='3acbe0f35016423f91efe655ca1bc14f').count()
    # data = ContentsSetupDataContract.delete('b2c94adca4c942e5a4022d2e529e1ad3')

    # data_check = ContentsSetupDataContract.objects.get('84ce26c2156344eab86581ff512d0674').delete()
    # data_check = ContentsSetupDataContract.objects.filter(content_setup_id='84ce26c2156344eab86581ff512d0674').delete()
    # print(data_check)
    print("today: ", datetime.datetime.today())
    print("tomorrow: ", datetime.datetime.today() + datetime.timedelta(days=1))
    # print(c)
    val = "<br><br><a href=\"{{ MEDIA_URL }}{{ filepath }}\" target=\"_blank\">{{ filename }}</a><br><br>"

    return HttpResponse('<b>Roll Test</b>')
    # return HttpResponse(get_content_types(request, "HTTP"))


def create_post(request):
    print('*** Sign up/Staff login post ****')
    print(json.dumps(request.POST))

    if request.method == 'POST':
        if request.POST.get('employeeSignupTag'):
            print("Tag: ", request.POST.get('employeeSignupTag'))
            # Sign up Employee and Staff login
            return HttpResponse(employee_signup(request))

        if request.POST.get('employeeLoginTag'):
            print("Tag: ", request.POST.get('employeeLoginTag'))
            # Staff login
            return HttpResponse(employee_login(request))

        if request.POST.get('createCountryTag'):
            print("Tag: ", request.POST.get('createCountryTag'))
            # Create a Country
            return HttpResponse(employee_login(request))
    else:
            return HttpResponse(json.dumps({'result': 'Not a POST request. No data. MAIN(3)'}),
                                content_type="application/json")


def setup_post(request):
    """
    For setup and configuration
    :param request:
    :return:
    """
    print('*** Setup post ****')
    print(json.dumps(request.POST))
    print(json.dumps(request.POST))
    tag = request.POST.get('ajaxRequestTag')

    if request.method == 'POST':
        print(tag)
        if tag == 'createCountryTag':
            print("Tag: ", tag)
            # Create a Country
            return HttpResponse(create_country(request))

        if tag == 'createCityTag':
            print("Tag: ", tag)
            # Create a City
            return HttpResponse(create_city(request))

        if tag == 'createAreaTag':
            print("Tag: ", tag)
            # Create a Area
            return HttpResponse(create_area(request))

        if tag == 'createDeviceTag':
            print("Tag: ", tag)
            # Create a Device
            return HttpResponse(create_device(request))

        if tag == 'createDeviceConfigTag':
            print("Tag: ", tag)
            # Create a Device Configuration
            return HttpResponse(create_device_config(request))

        if tag == 'createClusterTypeTag':
            print("Tag: ", tag)
            # Create a Cluster Type
            return HttpResponse(create_cluster_type(request))

        if tag == 'createClusterSetupTag':
            print("Tag: ", tag)
            # Create a Cluster Setup
            return HttpResponse(create_cluster_setup(request))

        if tag == 'createClusterNetworkConfigTag':
            print("Tag: ", tag)
            # Create a Cluster Network Configuration
            return HttpResponse(create_cluster_network_config(request))

        if tag == 'createContentTypeTag':
            print("Tag: ", tag)
            # Create a Content Type
            return HttpResponse(create_content_type(request))

        if tag == 'createClientProfileTag':
            print("Tag: ", tag)
            # Create a Client Profile
            return HttpResponse(create_client_profile(request))

        if tag == 'createContentSetupTag':
            print("++Tag: ", tag)
            print("Form contenting files uploading")
            # contentDataInput = request.FILES['contentDataInput']
            # contentContractDataInput = request.FILES['contentContractDataInput']
            #
            # if contentDataInput and contentContractDataInput:
            #     print("-----+++Yes+++------")
            # Create a Content Setup, data and contract file uploading
            return HttpResponse(create_content_setup_data_contract(request))

        if tag == 'createActiveClusterAndDevicesTag':
            print("Tag: ", tag)
            # Create a Active Cluster and Device
            return HttpResponse(create_active_cluster_and_devices(request))

        if tag == 'createActiveClusterAndContentsTag':
            print("Tag: ", tag)
            # Create a Active Cluster and Device
            return HttpResponse(create_active_cluster_and_contents(request))

    else:
            return HttpResponse(json.dumps({'result': 'Not a POST request. No data. MAIN(3)'}),
                                content_type="application/json")


def get_data_request(request):
    """
    Manages all get requests coming from web page
    :param request:
    :return:
    """
    print('*** Get data request ****')
    print(json.dumps(request.GET))
    tag = request.GET.get('ajaxRequestTag')

    if request.method == 'GET':
        # Fetch and return all data required on loading web app page
        if tag == 'onloadTag':
            # Fetch all onload data
            return HttpResponse(fetch_all_onload_data(request, 'DATA'))

        else:
            print("GET request issue")
    else:
        print('*** POST data request ****')
        print(json.dumps(request.POST))
        tag = request.POST.get('ajaxRequestTag')

        # Find/Fetch a Cluster Details
        if tag == 'findClusterDetailsTag':
            # Fetch
            return HttpResponse(fetch_cluster_details(request))
            # return HttpResponse(fetch_cluster_details(request, 'DATA'))


        return HttpResponse(json.dumps({'result': 'Not a GET request. No data. GDR(1)'}),
                            content_type="application/json")


def fetch_all_onload_data(request, return_type):
    """
    Fetch and return all data lists required onloading page
    :param request: HTTP request
    :param return_type: Different data list (such as Countries, Cities etc)
    :return:
    """
    response_data = {}

    response_data['employees'] = get_employees(request, return_type)
    response_data['countries'] = get_countries(request, return_type)
    response_data['cities'] = get_cities(request, return_type)
    response_data['areas'] = get_areas(request, return_type)
    response_data['devices'] = get_devices(request, return_type)
    response_data['clusterTypes'] = get_cluster_types(request, return_type)
    response_data['clusterSetups'] = get_active_cluster_setup(request, return_type)
    response_data['contentTypes'] = get_content_types(request, return_type)
    response_data['clientProfiles'] = get_client_profile(request, return_type)
    response_data['contentSetups'] = get_active_content_setup_data_contract(request, return_type)

    # print(response_data['clientProfiles'])

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def employee_signup(request):
    """
    Sign up/ set up Employee account and Staff login
    :param request:
    :return: HttpResponse object
    """

    print('*** Employee Sign Up ****')
    if request.method == 'POST':
        response_data = {}

        # Get form fields data
        last_name = request.POST.get('lastName').upper()
        first_name = request.POST.get('firstName').upper()
        office_tel = request.POST.get('employeeTel').upper()
        personal_tel = request.POST.get('personalTel').upper()
        office_email = request.POST.get('officeEmail').upper()
        personal_email = request.POST.get('personalEmail').upper()
        address = request.POST.get('homeAddress').upper()
        password = request.POST.get('signUpPass')

        try:
            # Check if Employee's account exist
            data_check = EmployeesProfile.objects.filter(employee_oemail=office_email)
            print("Employee's Email check : ", office_email)

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ". Employee email validation check failed. ES(1)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        if not data_check:
            try:
                # Employee Profile set up
                employee_data = EmployeesProfile(employee_lname=last_name, employee_fname=first_name, employee_tel=office_tel,
                                                 personal_tel=personal_tel, employee_oemail=office_email,
                                                 employee_pemail=personal_email, employee_address=address,
                                                 last_modified_user=office_email)
                employee_data.save()

            except ObjectDoesNotExist:
                response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ". Employee save validation failed. ES(2)"

                return HttpResponse(json.dumps(response_data), content_type="application/json")

            # Convert UUID value to String without (-) dashes
            employee_id = uuid.UUID(str(employee_data.employee_id)).hex

            try:
                # Staff login set up
                staff_login_data = StaffLogin(employee=EmployeesProfile.objects.get(employee_id=employee_id),
                                              login_password=password, last_modified_user=office_email)
                staff_login_data.save()

            except ObjectDoesNotExist:
                response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ". Employee's validation failed. ES(3)"

                return HttpResponse(json.dumps(response_data), content_type="application/json")

            # Response data
            response_data['result'] = 'Employee Profile is completed. Please login with your EMAIL and PASSWORD'
            response_data['lastName'] = employee_data.employee_lname

            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            print("Employee's account already Exist")
            # Already exist response message
            response_data['result'] = 'Employee Profile already exist'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        return HttpResponse(json.dumps({'result': 'Not a POST request. No data. ES(4)'}), content_type="application/json")


def get_employees(request, return_type):
    """
    Get list of Employee
    :param request:
    :return:
    """

    print('*** Get Employees ****')
    response_data = {}

    # Get Employees
    try:
        data_check = EmployeesProfile.objects.values('employee_oemail')
        print(str(data_check))

        if data_check:
            print('Employees data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('employee_oemail'))

            print('Response length: ', len(response_data))  # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Employees request failure. GE(1)"


def employee_login(request):
    """
    Staff login
    :param request:
    :return: HttpResponse object
    """

    print('*** Employee Login ****')
    if request.method == 'POST':
        response_data = {}

        # Get form fields data
        office_email = request.POST.get('loginEmail').upper()
        password = request.POST.get('loginPass')

        # Check if Employee's account exist
        try:
            employee = EmployeesProfile.objects.filter(employee_oemail=office_email).get()

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ". Staff's account validation failed. SL(1)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        print("*** Staff login's ID **** : ", employee.employee_id)

        # Check if Staff's login account exist
        try:
            data_check = StaffLogin.objects.filter(employee=EmployeesProfile.objects
                                                   .get(employee_id=employee.employee_id),
                                                   login_password=password).get()

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ". Staff's account validation failed. SL(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        # Return query data validation
        if data_check:
            print("*** Staff login validation PASSED!")
            # Response data
            response_data['result'] = 'Login validation passed'
            response_data['loginEmail'] = office_email

            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            print("*** Staff login validation FAILED!")
            # Failure response message
            response_data['result'] = 'Login validation failed'

            return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_country(request):
    """
    Create Country
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Country ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    country = request.POST.get('countryInput').upper()
    continent = request.POST.get('continentInput').upper()

    # Check if Country name exist
    try:
        data_check = Countries.objects.filter(country_name=country)
        print("Country check pass")

    except ObjectDoesNotExist:
        print("Country check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ".Country validation check failed. CC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If not country record found
    if not data_check:
        try:
            # Create a country
            country_data = Countries(country_name=country, continent=continent, last_modified_user=login_email)
            country_data.save()

            # Response data
            response_data['result'] = country_data.country_name + ' setup completed.'
            response_data['country'] = country_data.country_name

            # Get list of Countries after adding new Country
            print("Start countries fetch...")
            response_data[session_name] = get_countries(request, 'DATA')
            print("Countries fetch completed.")

            print(response_data)

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Country setup failed. CC(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Country account already exist")
        # Already exist response message
        response_data['result'] = 'Country already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_countries(request, return_type):
    """
    Get list of Countries
    :param request:
    :return:
    """

    print('*** Get Countries ****')
    response_data = {}

    # Get countries
    try:
        data_check = Countries.objects.values('country_name')
        print(str(data_check))

        if data_check:
            print('Counties data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('country_name'))

            print('Response length: ', len(response_data))  # Sanity check
            # print("Loop end")   # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Countries request failure. GC(1)"


def create_city(request):
    """
    Create City
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a City ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    country = request.POST.get('countryOfCityInput').upper()
    city_name = request.POST.get('cityNameInput').upper()

    # Check if City name exist
    try:
        data_check = Cities.objects.filter(city_name=city_name)
        print("City check pass")

    except ObjectDoesNotExist:
        print("City check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                      + ".City validation check failed. CC2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If not city record found
    if not data_check:
        try:
            # Find Country selected
            country_data = list(Countries.objects.filter(country_name=country).values('country_id'))
            print("Country check pass")

            # Convert >> country_id <<  UUID value to String without (-) dashes
            country_id = uuid.UUID(str(country_data[0].get('country_id'))).hex

            # Create a country
            city_data = Cities(country=Countries.objects.get(country_id=country_id), city_name=city_name,
                               last_modified_user=login_email)
            city_data.save()
            print("City save pass")

            # Response data
            response_data['result'] = city_data.city_name + ' setup completed.'
            response_data['city'] = city_data.city_name

            # Get list of Cities after adding new Device
            print("Start cities fetch...")
            response_data[session_name] = get_cities(request, 'DATA')
            print("Cities fetch completed.")

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". City setup failed. CC2(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("City account already exist")
        # Already exist response message
        response_data['result'] = 'City already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_cities(request, return_type):
    """

    :param request:
    :param return_type:
    :return:
    """

    print('*** Get Cities ****')
    response_data = {}

    # Get cities
    try:
        data_check = Cities.objects.values('city_name')
        print(str(data_check))

        if data_check:
            print('City data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('city_name'))

            print('Len: ', len(response_data))  # Sanity check
            print("Loop end")   # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get City request failure. GC(1)"


def create_area(request):
    """
    Create Area
    :param request:
    :return: HttpResponse object
    """

    print('*** Create an Area ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    city = request.POST.get('cityOfAreaInput').upper()
    area_name = request.POST.get('areaNameInput').upper()

    # Check if Area name exist
    try:
        data_check = Areas.objects.filter(area_name=area_name)
        print("Area check pass")

    except ObjectDoesNotExist:
        print("Area check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ".Area validation check failed. CA(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If not area record found
    if not data_check:
        try:
            # Find City selected
            city_data = list(Cities.objects.filter(city_name=city).values('city_id'))
            print("City check pass")

            # Convert >> city_id <<  UUID value to String without (-) dashes
            city_id = uuid.UUID(str(city_data[0].get('city_id'))).hex

            # Create an Area
            area_data = Areas(city=Cities.objects.get(city_id=city_id), area_name=area_name,
                              last_modified_user=login_email)
            area_data.save()
            print("Area save pass")

            # Response data
            response_data['result'] = area_data.area_name + ' setup completed.'
            response_data['area'] = area_data.area_name

            # Get list of Areas after adding new Device
            print("Start areas fetch...")
            response_data[session_name] = get_areas(request, 'DATA')
            print("Areas fetch completed.")

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Area setup failed. CA(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Area account already exist")
        # Already exist response message
        response_data['result'] = 'Area already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_areas(request, return_type):
    """

    :param request:
    :param return_type:
    :return:
    """

    print('*** Get Areas ****')
    response_data = {}

    # Get Areas
    try:
        data_check = Areas.objects.values('area_name')
        print(str(data_check))

        if data_check:
            print('Area data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('area_name'))

            print('Length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Area request failure. GC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_device(request):
    """
    Create Device
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Device ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    device_mac_address = request.POST.get('deviceMacAddressInput').upper()
    device_status = request.POST.get('deviceStatusInput').upper()

    # Check if Device name exist
    try:
        data_check = Devices.objects.filter(device_mac_address=device_mac_address)
        print("Device check pass")

    except ObjectDoesNotExist:
        print("Device check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) \
                                  + ".Device validation check failed. CD(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If not device record found
    if not data_check:
        try:
            # Create a Device
            device_data = Devices(device_mac_address=device_mac_address, device_status=device_status,
                                  last_modified_user=login_email)
            device_data.save()

            # Response data
            response_data['result'] = device_data.device_mac_address + ' setup completed.'
            response_data['device'] = device_data.device_mac_address

            # THIS WILL BE RECONSIDERED AS DEVICE LISTS GROW
            # Get list of Devices after adding new Device.
            print("Start devices fetch...")
            response_data[session_name] = get_devices(request, 'DATA')
            print("Devices fetch completed.")

            print(response_data)

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Device setup failed. CD(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Device account already exist")
        # Already exist response message
        response_data['result'] = 'Device already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_devices(request, return_type):
    """
    Get list of Devices
    :param request:
    :return:
    """

    print('*** Get Devices ****')
    response_data = {}

    # Get Devices
    try:
        data_check = Devices.objects.values('device_mac_address')
        print(str(data_check))

        if data_check:
            print('Devices data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('device_mac_address'))

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Devices request failure. GD(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_device_config(request):
    """
        Create Device Configuration
        :param request:
        :return: HttpResponse object
        """

    print('*** Create a Device Configuration ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    device_mac_address = request.POST.get('deviceOfDeviceConfigInput').upper()
    manufactured_year = request.POST.get('deviceManufacturedYearInput')
    extra_info = request.POST.get('deviceExtraInfoInput').upper()

    # Check if Device and Device configuration name exist
    try:
        device_data = list(Devices.objects.filter(device_mac_address=device_mac_address).values('device_id'))
        print("Device check pass")

        # Convert >> device_id <<  UUID value to String without (-) dashes
        device_id = uuid.UUID(str(device_data[0].get('device_id'))).hex
        print("device_id: " + device_id)

        # Check if Device Configuration exist
        device_config_check = list(DevicesConfiguration.objects.filter(device=device_id))

        # If Device Configuration record not found
        if not device_config_check:
            print("Device Configuration doesn't exist")

            # Create Device Configuration
            device_config_data = DevicesConfiguration(device=Devices.objects.get(device_id=device_id),
                                                      manufactured_year=manufactured_year, extra_info=extra_info,
                                                      last_modified_user=login_email)
            device_config_data.save()
            print("Device Configuration save pass")

            # Response data
            response_data['result'] = device_mac_address + ' configuration setup completed.'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Device Configuration setup already exist")
            # Already exist response message
            response_data['result'] = 'Device Configuration setup already exist'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Device Configuration check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Device Configuration validation check failed. CDC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_devices_configuration(request, return_type):
    """
    Get list of Devices Configuration
    :param request:
    :return:
    """

    print('*** Get Devices Configuration ****')
    response_data = {}

    # Get Device Configurations
    try:
        data_check = DevicesConfiguration.objects.values('device_config_id', 'manufactured_year', 'extra_info')
        print(str(data_check))

        if data_check:
            print('Devices Configuration data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), (data[i].get('device_config_id') + " - "
                                         + data[i].get('manufactured_year')
                                         + " - " + data[i].get('extra_info')))
                # response_data.setdefault(str(i), data[i].get('device_config_id'))

            print('Response length: ', len(response_data))  # Sanity check
            print("**************")    # Sanity check
            print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Devices Configuration request failure. GD(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_cluster_type(request):
    """
    Create Cluster Type
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Cluster Type ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    cluster_location_type = request.POST.get('clusterTypeInput').upper()

    # Check if Cluster Type name exist
    try:
        data_check = ClusterTypes.objects.filter(cluster_location_type=cluster_location_type)
        print("Cluster Type check pass")

    except ObjectDoesNotExist:
        print("Cluster Type check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) \
                                  + ".Device validation check failed. CCT(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If no Cluster Type record found
    if not data_check:
        try:
            # Create a Cluster Type
            cluster_type_data = ClusterTypes(cluster_location_type=cluster_location_type,
                                             last_modified_user=login_email)
            cluster_type_data.save()

            # Response data
            response_data['result'] = cluster_type_data.cluster_location_type + ' setup completed.'
            # response_data['clusterType'] = cluster_type_data.device_mac_address

            # Get list of Cluster Types after adding new Cluster Type.
            print("Start Cluster Types fetch...")
            response_data[session_name] = get_cluster_types(request, 'DATA')
            print("Cluster Types fetch completed.")

            print(response_data)

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Cluster Type setup failed. CCT(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Cluster Type already exist")
        # Already exist response message
        response_data['result'] = 'Cluster Type already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_cluster_types(request, return_type):
    """
    Get list of Cluster Types
    :param request:
    :return:
    """

    print('*** Get Cluster Types ****')
    response_data = {}

    # Get Cluster Types
    try:
        data_check = ClusterTypes.objects.values('cluster_location_type')
        print(str(data_check))

        if data_check:
            print('Cluster Type(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('cluster_location_type'))

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Cluster Type(s) request failure. GCT2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_cluster_setup(request):
    """
        Create Cluster Setup
        :param request:
        :return: HttpResponse object
        """

    print('*** Create a Cluster Setup ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    area_name = request.POST.get('clusterSetupOfAreaInput').upper()
    cluster_location_type = request.POST.get('clusterTypeOfClusterSetupInput')
    cluster_location_detail = request.POST.get('clusterLocationDetailInput').upper()
    cluster_exposure = request.POST.get('clusterExposureInput').upper()
    cluster_status = request.POST.get('clusterStatusInput').upper()

    # Check if Area and/or Cluster Type already exist in Cluster Setup table
    try:
        area_data = Areas.objects.filter(area_name=area_name).values('area_id')
        print("Area check pass")
        print(area_data)

        cluster_type_data = ClusterTypes.objects.filter(cluster_location_type=cluster_location_type).values('cluster_type_id')
        print("Cluster Type check pass")
        print(cluster_type_data)

        # Convert >> area_id <<  UUID value to String without (-) dashes
        area_id = uuid.UUID(str(area_data[0].get('area_id'))).hex
        print("area_id: " + area_id)

        # Convert >> cluster_type_id <<  UUID value to String without (-) dashes
        cluster_type_id = uuid.UUID(str(cluster_type_data[0].get('cluster_type_id'))).hex
        print("cluster_type_id: " + cluster_type_id)

        # Check if Cluster Setup exist
        # cluster_setup_check = ClustersSetup.objects.filter(area=area_id, cluster_type=cluster_type_id)
        cluster_setup_check = ClustersSetup.objects.filter(area=area_id,
                                                           cluster_location_detail=cluster_location_detail)

        # If Cluster Setup record not found
        if not cluster_setup_check:
            print("Cluster Setup doesn't exist")
            print(cluster_setup_check)

            # Create Cluster Setup
            cluster_setup_data = ClustersSetup(area=Areas.objects.get(area_id=area_id),
                                               cluster_type=ClusterTypes.objects.get(cluster_type_id=cluster_type_id)   ,
                                               cluster_location_detail=cluster_location_detail,
                                               cluster_exposure=cluster_exposure, cluster_status=cluster_status,
                                               last_modified_user=login_email)
            cluster_setup_data.save()
            print("Cluster Setup save pass")

            # Response data
            response_data['result'] = 'Cluster Setup in ' + area_name + ' at ' + cluster_location_detail + ' completed.'

            # Get list of Cluster Types after adding new Cluster Type.
            print("Start Cluster Setups fetch...")
            response_data[session_name] = get_active_cluster_setup(request, 'DATA')
            print("Cluster Setups fetch completed.")

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Cluster Setup setup already exist")
            # Already exist response message
            response_data['result'] = 'Cluster Setup already exist'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Cluster Setup check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Cluster Setup validation check failed. CCS(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_active_cluster_setup(request, return_type):
    """
    Get list of Active Cluster Setup
    :param request:
    :return: HttpResponse object
    """

    print('*** Get Active Cluster Setup ****')
    response_data = {}
    active_cluster_status = 'ACTIVE'
    unused_cluster_status = 'UNUSED'

    # Get Cluster Setup
    try:
        data_check = ClustersSetup.objects.filter(Q(cluster_status=active_cluster_status) |
                                                  Q(cluster_status=unused_cluster_status))\
            .values('cluster_location_detail')
        print(str(data_check))

        if data_check:
            print('Active Cluster Setup(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                # response_data.setdefault(str(i), (data[i]))
                response_data.setdefault(str(i), (data[i].get('cluster_location_detail')))

            print('Response length: ', len(response_data))  # Sanity check
            print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Active Cluster Setup request failure. AGCS(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_cluster_setup(request, return_type):
    """
    Get list of Cluster Setup
    :param request:
    :return: HttpResponse object
    """

    print('*** Get Cluster Setup ****')
    response_data = {}

    # Get Cluster Setup
    try:
        data_check = ClustersSetup.objects.values('cluster_location_detail')
        print(str(data_check))

        if data_check:
            print('Cluster Setup(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                # response_data.setdefault(str(i), (data[i]))
                response_data.setdefault(str(i), (data[i].get('cluster_location_detail')))
                #                                   + " - " + data[i].get('cluster_location_detail')
                #                                   + " - " + data[i].get('cluster_exposure')
                #                                   + " - " + data[i].get('cluster_status')))
                # response_data.setdefault(str(i), data[i].get('device_config_id'))

            print('Response length: ', len(response_data))  # Sanity check
            print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Cluster Setup request failure. GCS(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_cluster_network_config(request):
    """
        Create Cluster Network Configuration
        :param request:
        :return: HttpResponse object
        """

    print('*** Create a Cluster Network Configuration ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    cluster_setup = request.POST.get('clusterSetupOfClusterNetConfigInput').upper()
    cluster_network_provider = request.POST.get('clusterNetworkProviderInput')
    cluster_network_pass = request.POST.get('clusterNetworkPassInput').upper()

    # Check if Cluster Setup already exist in Cluster Network Configuration table
    try:
        cluster_setup_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup)\
            .values('cluster_setup_id')
        print("Cluster Network Configuration check pass")
        print(cluster_setup_data)

        # Convert >> area_id <<  UUID value to String without (-) dashes
        cluster_setup_id = uuid.UUID(str(cluster_setup_data[0].get('cluster_setup_id'))).hex
        print(cluster_setup_data)

        # Check if Cluster Network Configuration exist
        cluster_network_config_check = ClustersNetworkConfiguration.objects.filter(cluster_setup=cluster_setup_id)

        # If Cluster Network Configuration record not found
        if not cluster_network_config_check:
            print("Cluster Network Configuration doesn't exist")
            print(cluster_network_config_check)

            # Create Cluster Network Configuration
            cluster_network_config_data = ClustersNetworkConfiguration(cluster_setup=ClustersSetup.objects
                                                                       .get(cluster_setup_id=cluster_setup_id),
                                                                       cluster_network_provider=cluster_network_provider,
                                                                       cluster_network_pass=cluster_network_pass,
                                                                       last_modified_user=login_email)
            cluster_network_config_data.save()
            print("Cluster Network Configuration save pass")

            # Response data
            response_data['result'] = cluster_setup + ' Network Configuration completed.'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Cluster Network Configuration already exist")
            # Already exist response message
            response_data['result'] = 'Cluster Network Configuration already exist. Only one network ' \
                                      'configuration is allowed.'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Cluster Network Configuration check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Cluster Network Configuration validation check failed. CCNCS(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_cluster_network_config(request, return_type):
    """
    Get list of Cluster Network Configuration
    :param request:
    :return: HttpResponse object
    """

    print('*** Get Cluster Network Configuration ****')
    response_data = {}

    # Get Cluster Network Configuration
    try:
        data_check = ClustersNetworkConfiguration.objects.values('cluster_network_provider')
        print(str(data_check))

        if data_check:
            print('Cluster Network Configuration(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), (data[i].get('cluster_network_provider')))

            print('Response length: ', len(response_data))  # Sanity check
            print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Cluster Network Configuration request failure. GCNCS(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_content_type(request):
    """
    Create Content Type
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Content Type ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    content_type_name = request.POST.get('contentTypeInput').upper()

    # Check if Cluster Type name exist
    try:
        data_check = ContentTypes.objects.filter(content_type_name=content_type_name)
        print("Content Type check pass")

    except ObjectDoesNotExist:
        print("Content Type check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) \
                                  + ". Content Type validation check failed. CCT2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If no Content Type record found
    if not data_check:
        try:
            # Create a Content Type
            content_type_data = ContentTypes(content_type_name=content_type_name,
                                             last_modified_user=login_email)
            content_type_data.save()

            # Response data
            response_data['result'] = content_type_data.content_type_name + ' setup completed.'

            # Get list of Content Types after adding new Content Type.
            print("Start Content Types fetch...")
            response_data[session_name] = get_content_types(request, 'DATA')
            print("Content Types fetch completed.")

            print(response_data)

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Content Type setup failed. CCT2(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Content Type already exist")
        # Already exist response message
        response_data['result'] = 'Content Type already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_content_types(request, return_type):
    """
    Get list of Content Types
    :param request:
    :return:
    """

    print('*** Get Content Types ****')
    response_data = {}

    # Get Content Types
    try:
        data_check = ContentTypes.objects.values('content_type_name')
        print(str(data_check))

        if data_check:
            print('Content Type(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('content_type_name'))
                # print(response_data)

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return response_data
                # return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Content Type(s) request failure. GCT2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_client_profile(request):
    """
    Create Client Profile
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Client Profile ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    client_name = request.POST.get('clientNameInput').upper()
    client_tel = request.POST.get('clientTelInput').upper()
    contact_person = request.POST.get('clientContactPersonInput').upper()
    client_email = request.POST.get('clientEmailInput').upper()
    client_address = request.POST.get('clientAddressInput').upper()

    # Check if Client Profile name exist
    try:
        data_check = ClientsProfile.objects.filter(client_name=client_name)
        print("Client Profile check pass")

    except ObjectDoesNotExist:
        print("Client Profile check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) \
                                  + ". Client Profile validation check failed. CCP(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    # If no Client Profile record found
    if not data_check:
        try:
            # Create a Client Profile
            client_profile_data = ClientsProfile(client_name=client_name, client_tel=client_tel,
                                                 contact_person=contact_person, client_email=client_email,
                                                 client_address=client_address, last_modified_user=login_email)
            client_profile_data.save()

            # Response data
            response_data['result'] = client_profile_data.client_name + ' setup completed.'

            # Get list of Client Profile after adding new Content Type.
            print("Start Client Profile fetch...")
            response_data[session_name] = get_client_profile(request, 'DATA')
            print("Client Profile fetch completed.")

            print(response_data)

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except ObjectDoesNotExist:
            response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                      ". Client Profile setup failed. CCP(2)"

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        print("Client Profile already exist")
        # Already exist response message
        response_data['result'] = 'Client Profile already exist'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_client_profile(request, return_type):
    """
    Get list of Client Profile
    :param request:
    :return:
    """

    print('*** Get Client Profiles ****')
    response_data = {}

    # Get Client Profile
    try:
        data_check = ClientsProfile.objects.values('client_name')
        print(str(data_check))

        if data_check:
            print('Client Profile(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('client_name'))
                # print(response_data)

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return response_data
        else:
            response_data["none"] = "NO DATA"

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Client Profile(s) request failure. GCP2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_content_setup_data_contract(request):
    """
    Create Content Setup
    :param request:
    :return: HttpResponse object
    """

    print('*** Create a Content Setup ****')
    response_data = {}

    # Get session name
    session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    content_type = request.POST.get('contentTypeOfContentSetupInput').upper()
    content_title = request.POST.get('contentTitleInput').upper()
    is_content_new = request.POST.get('isContentNewInput')
    client = request.POST.get('clientProfileOfContentSetupInput').upper()
    our_representative = request.POST.get('employeeOfContentSetupInput').upper()
    fee_paid = request.POST.get('contentContractFeeInput')
    start_date = request.POST.get('contentContractStartInput')
    end_date = request.POST.get('contentContractEndInput')
    content_data = request.FILES['contentDataInput']
    # content_data = request.FILES.get('contentDataInput')
    content_contract_data = request.FILES['contentContractDataInput']
    # content_contract_data = request.FILES.get('contentContractDataInput')

    print("test print data files")
    print(content_data)
    print(content_contract_data)
    # Check if Content Type and Content Tile already exist Content Setup table
    try:
        content_type_data = ContentTypes.objects.filter(content_type_name=content_type).values('content_type_id')
        print("Content type check pass")
        print(content_type_data)

        client_data = ClientsProfile.objects.filter(client_name=client).values('client_id')
        print("Content type check pass")
        print(content_type_data)

        employee_data = EmployeesProfile.objects.filter(employee_oemail=our_representative).values('employee_id')
        print("Employee check pass")
        print(employee_data)

        # Convert >> content_type_id <<  UUID value to String without (-) dashes
        content_type_id = uuid.UUID(str(content_type_data[0].get('content_type_id'))).hex
        print("area_id: " + content_type_id)

        # Convert >> client_id <<  UUID value to String without (-) dashes
        client_id = uuid.UUID(str(client_data[0].get('client_id'))).hex
        print("client_id: " + client_id)

        # Convert >> employee_id <<  UUID value to String without (-) dashes
        employee_id = uuid.UUID(str(employee_data[0].get('employee_id'))).hex
        print("employee_id: " + employee_id)

        # Check if Content Setup exist
        content_setup_check = ContentsSetupDataContract.objects.filter(Q(content_type=content_type_id,
                                                                       content_title=content_title) |
                                                                       Q(content_title=content_title))
        # If Content Setup record not found
        if not content_setup_check:
            print("Content Setup doesn't exist")
            print(content_setup_check)

            # Create Content Setup
            cluster_setup_data = ContentsSetupDataContract(content_type=ContentTypes.objects
                                                           .get(content_type_id=content_type_id),
                                                           client=ClientsProfile.objects.get(client_id=client_id),
                                                           our_representative=EmployeesProfile
                                                           .objects.get(employee_id=employee_id),
                                                           content_title=content_title, is_content_new=is_content_new,
                                                           fee_paid=fee_paid, start_date=start_date, end_date=end_date,
                                                           content_data=content_data,
                                                           content_contract_data=content_contract_data,
                                                           last_modified_user=login_email)
            cluster_setup_data.save()
            print("Content Setup save pass")

            # Response data
            response_data['result'] = 'Content Setup titled ' + content_title + ' setup completed.'

            # Get list of Content Setups after adding new Content Type.
            print("Start Content Setups fetch...")
            response_data[session_name] = get_active_content_setup_data_contract(request, 'DATA')
            print("Content Setups fetch completed.")

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Content Setup setup already exist")
            # Already exist response message
            response_data['result'] = 'Content Setup already exist. Please ensure the Content is Unique.    '

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Content Setup check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Content Setup validation check failed. CCS2(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_active_content_setup_data_contract(request, return_type):
    """
    Get list of Active Content Setup, data, contract etc
    :param request:
    :return:
    """

    print('*** Get Active Content Setup ****')
    response_data = {}

    # Get Content Setup with start in future (i.e greater than today)
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    try:
        data_check = ContentsSetupDataContract.objects.filter(start_date__gte=tomorrow).values('content_title')
        print(str(data_check))

        if data_check:
            print('Content Setup(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('content_title'))
                # print(response_data)

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Content Setup(s) request failure. GCSDC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_content_setup_data_contract(request, return_type):
    """
    Get list of Content Setup, data, contract etc
    :param request:
    :return:
    """

    print('*** Get Content Setup ****')
    response_data = {}

    # Get Content Setup
    try:
        data_check = ContentsSetupDataContract.objects.values('content_title')
        print(str(data_check))

        if data_check:
            print('Content Setup(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                response_data.setdefault(str(i), data[i].get('content_title'))
                # print(response_data)

            print('Response length: ', len(response_data))  # Sanity check
            # print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Content Setup(s) request failure. GCSDC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_active_cluster_and_devices(request):
    """
        Create and assign an Active Cluster with Devices
        :param request:
        :return: HttpResponse object
        """

    print('*** Create an Active Cluster with Devices ****')
    # Variable declarations
    response_data = {}
    status_check = ['ACTIVE', 'DEACTIVATED']

    # Get session name
    #session_name = request.POST.get('sessionName')

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    cluster_setup = request.POST.get('clusterSetupOfActiveCandDeviceInput')
    device = request.POST.get('deviceOfActiveCandDeviceInput').upper()

    # Check if Active Cluster and Device exist. Check if the numbers of
    # Contents displaying (i.e. Content Setup) are less 10.
    try:
        # Checks if Active Cluster Setup Name exist
        cluster_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup).values('cluster_setup_id',
                                                                                                  'cluster_status')
        print("Active Cluster Setup check pass")
        print(cluster_data)

        # Checks if Device MAC Name exist - THIS SEARCH CAN BE NARROW DOWN TO COUNTRY - CITY - AREA
        device_data = Devices.objects.filter(device_mac_address=device).values('device_id', 'device_status')
        print("Device check pass")
        print(device_data)

        device_status = str(device_data[0].get('device_status'))

        # Check if Device is available for use
        if device_status in status_check:
            print('Device is ', device_status)

            # Response data
            response_data['result'] = 'Device ' + device + ' is currently ' + device_status + '. Not available for use.'
            #
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        # Convert >> cluster_setup_id <<  UUID value to String without (-) dashes
        cluster_setup_id = uuid.UUID(str(cluster_data[0].get('cluster_setup_id'))).hex
        print("cluster_setup_id: " + cluster_setup_id)

        # Convert >> device_id <<  UUID value to String without (-) dashes
        device_id = uuid.UUID(str(device_data[0].get('device_id'))).hex
        print("device_id: " + device_id)

        # Check if the combination of Active Cluster, Content and Device exist
        active_cluster_and_device_check = ActiveClustersAndDevices.objects.filter(cluster_setup=cluster_setup_id,
                                                                                  device=device_id)

        # If Active Cluster and Device record not found
        if not active_cluster_and_device_check:
            print("Active_cluster_and_device doesn't exist")
            print(active_cluster_and_device_check)

            # Create Active Cluster and Device
            active_cluster_and_device_data = ActiveClustersAndDevices(cluster_setup=ClustersSetup.objects.
                                                                      get(cluster_setup_id=cluster_setup_id),
                                                                      device=Devices.objects.get(device_id=device_id),
                                                                      last_modified_user=login_email)
            active_cluster_and_device_data.save()
            print("Active Cluster, Content and Device save pass")

            # Update Device Status to ACTIVE
            device_update = Devices.objects.filter(device_mac_address=device)
            device_update.update(device_status=status_check[0])

            print("Device Updated to: ", device_update)

            # Response data
            response_data['result'] = device + ' is now added to ' + cluster_setup + ' cluster.'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Active Cluster and Device setup already exist")
            # Already exist response message
            response_data['result'] = 'Active Cluster and Device setup already exist'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Active Cluster and Device Setup check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Active Cluster and Device Setup validation check failed. CACAD(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def create_active_cluster_and_contents(request):
    """
        Create and assign an Active Cluster with Content for display
        :param request:
        :return: HttpResponse object
        """

    print('*** Create an Active Cluster with Content for display ****')
    # Variable declarations
    response_data = {}
    display_content_limit = 10

    # Get session name
    session_name = request.POST.get('sessionName')
    status_check = ['ACTIVE', 'UNUSED']

    # Get form fields data
    login_email = request.POST.get('loginEmail').upper()
    cluster_setup = request.POST.get('clusterSetupOfActiveCandContentInput')
    content_setup = request.POST.get('contentSetupOfActiveCandContentInput')
    # device = request.POST.get('deviceOfActiveCandDeviceInput').upper()
    print(cluster_setup)
    print(content_setup)

    # Check if Active Cluster and Contents Setup exist. Check if the numbers of
    # Contents displaying (i.e. Content Setup) are less 10.
    try:
        # Checks if Active Cluster Setup Name exist
        cluster_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup).values('cluster_setup_id',
                                                                                                  'cluster_status')
        print("Active Cluster Setup check pass")
        print(cluster_data)

        # Check if Cluster is Active or Unused. If UNUSED, make it ACTIVE and proceed.
        current_cluster_status = str(cluster_data[0].get('cluster_status'))
        print("current_cluster_status 1: ", current_cluster_status)

        if current_cluster_status == status_check[1]:
            print("current_cluster_status 2: ", current_cluster_status)
            # Update Device Status to ACTIVE
            cluster_data.update(cluster_status=status_check[0])

        # Checks if Content Setup, Data and Contract id exist and count is less or equal 10
        # in ActiveClustersAndDevices table
        content_setup_data = ContentsSetupDataContract.objects.filter(content_title=content_setup) \
            .values('content_setup_id')
        print("Active Content Setup check pass")
        print(content_setup_data)

        # Convert >> cluster_setup_id <<  UUID value to String without (-) dashes
        cluster_setup_id = uuid.UUID(str(cluster_data[0].get('cluster_setup_id'))).hex
        print("cluster_setup_id: " + cluster_setup_id)

        # Convert >> content_setup_id <<  UUID value to String without (-) dashes
        content_setup_id = uuid.UUID(str(content_setup_data[0].get('content_setup_id'))).hex
        print("cluster_setup_id: " + content_setup_id)

        # Check numbers of ContentsSetupDataContract is equal allowed limit (i.e display_content_limit) in the
        # ActiveClustersAndContents table
        active_cluster_content_limit_check = ActiveClustersAndContents.objects \
            .filter(cluster_setup=cluster_setup_id).count()

        print("Limit Count: ", active_cluster_content_limit_check)
        if active_cluster_content_limit_check >= display_content_limit:
            # Response data
            response_data['result'] = "This Cluster " + cluster_setup + " has reached its maximum " + \
                                      str(display_content_limit) + " allowed Displaying Content."

            return HttpResponse(json.dumps(response_data), content_type="application/json")

        # Check if the combination of Active Cluster and Content exist
        active_cluster_and_content_check = ActiveClustersAndContents.objects.filter(cluster_setup=cluster_setup_id,
                                                                                    content_setup=content_setup_id)

        # If Active Cluster and Content record not found
        if not active_cluster_and_content_check:
            print("Active_cluster_and_Content doesn't exist")
            print(active_cluster_and_content_check)

            # Create Active Cluster and Content
            active_cluster_and_Content_data = ActiveClustersAndContents(cluster_setup=ClustersSetup.objects
                                                                        .get(cluster_setup_id=cluster_setup_id),
                                                                        content_setup=ContentsSetupDataContract.objects
                                                                        .get(content_setup_id=content_setup_id),
                                                                        last_modified_user=login_email)
            active_cluster_and_Content_data.save()
            print("Active Cluster and Content save pass")

            # Response data
            response_data['result'] = content_setup + ' is now added to ' + cluster_setup + ' cluster.'

            # # Get list of Active Cluster and Content after adding new Cluster Type.
            # print("Start Cluster Setups fetch...")
            # response_data[session_name] = get_cluster_setup(request, 'DATA')
            # print("Cluster Setups fetch completed.")
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        else:
            print("Active Cluster and Content setup already exist")
            # Already exist response message
            response_data['result'] = 'Active Cluster and Content setup already exist'

            return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Active Cluster and Content Setup check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Active Cluster and Content Setup validation check failed. CACC(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


# TO-DO
def get_active_cluster_and_devices(request, return_type):
    """
    Get list of Active Cluster, Content and Device Setup
    :param request:
    :return: HttpResponse object
    """

    print('*** Get Active Cluster, Content and Device Setup ****')
    response_data = {}

    # Get Active Cluster, Content and Device Setup
    try:
        data_check = ClustersSetup.objects.values('cluster_location_detail')
        print(str(data_check))

        if data_check:
            print('Active Cluster, Content and Device Setup(s) data found')
            data = list(data_check)

            for i in range(len(data)):
                # response_data.setdefault(str(i), (data[i]))
                response_data.setdefault(str(i), (data[i].get('cluster_location_detail')))

            print('Response length: ', len(response_data))  # Sanity check
            print(response_data)    # Sanity check

            if return_type == 'HTTP':
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                return response_data

        else:
            response_data["none"] = "NO DATA"
            # print(response_data)

            return response_data

    except ObjectDoesNotExist:
        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure) + \
                                  ". Get Active Cluster, Content and Device Setup request failure. GACCAD(1)"

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def fetch_cluster_details(request):
    """
        Fetch Cluster Details
        :param request:
        :return: HttpResponse object
    """

    print('*** Fetch Cluster Details ****')
    # Variable declarations
    response_data = {}
    content_dir = '/contents/'

    # Get session name
    # session_name = request.POST.get('sessionName')

    # Get form fields data
    # login_email = request.POST.get('loginEmail')
    # city_name = request.POST.get('cityOfClusterDetailsInput')
    # area_name = request.POST.get('areaOfClusterDetailsInput')
    cluster_setup = request.POST.get('clusterSetupOfClusterDetailsInput')

    # Start Active Cluster detail search
    try:
        # Find Active Cluster details
        cluster_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup)\
            .values('cluster_status', 'cluster_location_detail', 'cluster_exposure',
                    'cluster_type__cluster_location_type', 'cluster_type__last_modified_user')

        print("Active Cluster Setup check pass")
        print(cluster_data)
        response_data['Cluster Detail'] = list(cluster_data)
        # print(response_data)

        device_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup)\
            .values('ActiveClusterAndDevice__device__device_mac_address',
                    'ActiveClusterAndDevice__device__device_status',
                    'ActiveClusterAndDevice__last_modified_user')
        response_data['Devices'] = list(device_data)
        # print(response_data)

        content_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_setup)\
            .values('ActiveClusterAndContent__content_setup__content_type__content_type_name',
                    'ActiveClusterAndContent__content_setup__content_title',
                    'ActiveClusterAndContent__content_setup__content_data',
                    'ActiveClusterAndContent__content_setup__client__client_name',
                    'ActiveClusterAndContent__content_setup__our_representative__employee_oemail',
                    'ActiveClusterAndContent__content_setup__start_date',
                    'ActiveClusterAndContent__content_setup__end_date',
                    'ActiveClusterAndContent__content_setup__last_modified_user')

        response_data['Contents'] = list(content_data)
        # print(response_data)

        for key in response_data['Contents']:
            # Modify date format
            start_date = key.get('ActiveClusterAndContent__content_setup__start_date').strftime('%m/%d/%Y')
            key['ActiveClusterAndContent__content_setup__start_date'] = start_date

            end_date = key.get('ActiveClusterAndContent__content_setup__end_date').strftime('%m/%d/%Y')
            key['ActiveClusterAndContent__content_setup__end_date'] = end_date

            # Add/Modify file path
            file_name = key.get('ActiveClusterAndContent__content_setup__content_data')
            key['ActiveClusterAndContent__content_setup__content_data'] = content_dir + file_name

        print("***********************-------------------+++++++++++++++++++++++++")
        print(response_data)

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except ObjectDoesNotExist:
        print("Fetch Cluster Details check failed")

        response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                  + ". Fetch Cluster Details validation check failed. FCD(1)"


def device_request(request):
    """
        Fetch Device media contents for devices
        :param request:
        :return: HttpResponse object
    """

    print('*** Fetch Device media contents for devices ****')
    # Variable declarations
    get_data = request.GET
    response_data = {}
    content_dir = '/contents/'

    # Ensures request method is a GET
    if request.method == 'GET' and len(request.GET) != 0:
        # print(len(request.GET))

        if 'cName' in get_data:
            print('Request from a Pod device')

            try:

                cluster_name = get_data.get('cName')
                content_data = ClustersSetup.objects.filter(cluster_location_detail=cluster_name) \
                    .values('ActiveClusterAndContent__content_setup__content_data')

                response_data['Contents'] = list(content_data)

                print(response_data)

                result_data = {}
                count = 0
                for key in response_data['Contents']:
                    count = count + 1
                    # Add/Modify file path
                    file_name = key.get('ActiveClusterAndContent__content_setup__content_data')
                    result_data[count] = content_dir + file_name

                return HttpResponse(json.dumps(result_data), content_type="application/json")

            except ObjectDoesNotExist:
                print("Fetch Device media contents for devices check failed")

                response_data['result'] = "ERROR Status: " + str(ObjectDoesNotExist.silent_variable_failure)\
                                          + ". Fetch Device media contents for devices validation check failed. DR(1)"


def show_contents_data(request):
    print('*** Show contents data ****')

    last_content_data = Test.objects.last()
    print(last_content_data)

    if last_content_data:
        content_file = last_content_data.content_data
        context = {'content_file': content_file}

        print("Queries:")
        print(connection.queries)
    #
        return render(request, 'pages/dashboardTest.html', context)


def create_contents_data(request):
    print(json.dumps(request.POST))
    # file = request.FILES.myfile
    file = request.FILES['myfile']

    if request.method == 'POST' and file:
        print("in create_contents_data")

        title = request.POST.get('title')
        file_name = file.name
        print("_+_+_+_++: ", title)
        print("File:_+_+_+_++: ", file_name)

        data = Test(content_title=title, content_data=file)
        data.save()
        # print(list(data))

        last_content_data = Test.objects.last()
        print(last_content_data)

        if last_content_data:
            content_file = last_content_data.content_data
            context = {'content_file': content_file}
            print(content_file)

            return render(request, 'pages/dashboardTest.html', context)

        else:
            return render(request, 'pages/dashboardTest.html')