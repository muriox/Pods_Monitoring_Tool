from django.db import models
import uuid


class Countries(models.Model):
    """
        1 COUNTRIES TABLE
    """
    country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_name = models.CharField(max_length=80, null=False)
    continent = models.CharField(max_length=80, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True)

    objects = models.QuerySet()

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "Countries"


class Cities(models.Model):
    """
       2 CITIES TABLE
    """
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, null=False, related_name='cities',
                                related_query_name='city')
    city_name = models.CharField(max_length=100, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = "Cities"


class Areas(models.Model):
    """
       3 AREA TABLE
    """
    area_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, null=False, related_name='areas',
                             related_query_name='area')
    area_name = models.CharField(max_length=100, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.area_id + " - " + self.area_name

    class Meta:
        verbose_name_plural = "Areas"


class Devices(models.Model):
    """
       4 DEVICES TABLE
    """
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_mac_address = models.CharField(max_length=50, null=False)
    # Device used in a Cluster = ACTIVE; not used in any Cluster = UNUSED; others = IN-REPAIR, DEACTIVATED
    device_status = models.CharField(max_length=50, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.device_mac_address + " - " + self.device_status

    class Meta:
        verbose_name_plural = "Devices"


class DevicesConfiguration(models.Model):
    """
       5 DEVICES CONFIGURATION
    """
    device_config_id = models.AutoField(primary_key=True, null=False)
    device = models.OneToOneField(Devices, on_delete=models.PROTECT, null=False, related_name='deviceConfigurations',
                                  related_query_name='deviceConfiguration')
    manufactured_year = models.DateField()  # YYYY-MM-DD format

    # Extra info
    extra_info = models.CharField(max_length=514, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.device_config_id + " - " + self.device.device_mac_address

    class Meta:
        verbose_name_plural = "DevicesConfiguration"


class ClusterTypes(models.Model):
    """
       6 CLUSTER TYPES TABLE
    """
    cluster_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # cluster_location_type: Highway, Street, Train Station, Bus Station, University, College,
    #                        High School, Primary School, Event Centre, Sport Center, Stores etc.
    cluster_location_type = models.CharField(max_length=50, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.cluster_type_id + " - " + self.cluster_location_type

    class Meta:
        verbose_name_plural = "ClusterTypes"


class ClustersSetup(models.Model):
    """
       7 CLUSTERS SETUP TABLE
    """
    cluster_setup_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area = models.ForeignKey(Areas, on_delete=models.PROTECT, null=False, related_name='clusterSetups',
                             related_query_name='clusterSetup')
    cluster_type = models.ForeignKey(ClusterTypes, on_delete=models.PROTECT, null=False, related_name='clusterSetups',
                                     related_query_name='clusterSetup')
    # More specific description of location, such as Postcode, building, detailed address etc
    cluster_location_detail = models.CharField(max_length=80, null=False)
    # Indoor or Output
    cluster_exposure = models.CharField(max_length=8, null=False)
    cluster_status = models.CharField(max_length=50, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.cluster_setup_id + " - " + self.cluster_location_detail

    class Meta:
        verbose_name_plural = "ClustersSetup"


class ClustersNetworkConfiguration(models.Model):
    """
       8 CLUSTERS NETWORK CONFIGURATION TABLE
    """
    clusters_network_config_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_setup = models.ForeignKey(ClustersSetup, on_delete=models.PROTECT, null=False,
                                      related_name='clustersNetworkConfigurations',
                                      related_query_name='clustersNetworkConfiguration')

    # Network provider of (Wi-Fi/wireless network)
    cluster_network_provider = models.CharField(max_length=50, null=False)
    cluster_network_pass = models.CharField(max_length=128, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.clusters_network_config_id + " - " + self.cluster_network_provider

    class Meta:
        verbose_name_plural = "ClustersNetworkConfiguration"


class ClustersWeatherCondition(models.Model):
    """
       9 CLUSTERS WEATHER CONDITION TABLE
    """
    clusters_weather_condition_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_setup = models.ForeignKey(ClustersSetup, on_delete=models.PROTECT, null=False,
                                      related_name='clustersWeatherConditions',
                                      related_query_name='clustersWeatherCondition')

    # Geo-location
    latitude = models.CharField(max_length=100, null=False)
    longitude = models.CharField(max_length=100, null=False)

    # JSON data description
    cluster_json_data = models.CharField(max_length=128, null=True)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.clusters_weather_condition_id + " - Lat:" + self.latitude + "; Long:" + self.longitude

    class Meta:
        verbose_name_plural = "ClustersWeatherCondition"


# class ClustersDetails(models.Model):
#     """
#        10 CLUSTERS DETAILS TABLE - not relevant yet
#     """
#     clusters_details_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     cluster_setup_id = models.ForeignKey(ClustersSetup, on_delete=models.PROTECT, primary_key=True, null=False)
#     clusters_network_config_id = models.ForeignKey(ClustersNetworkConfiguration, on_delete=models.PROTECT,
#                                                    primary_key=True, null=False)
#     clusters_weather_condition_id = models.ForeignKey(ClustersWeatherCondition, on_delete=models.PROTECT,
#                                                       primary_key=True, null=False)
#
#     last_modified_user = models.CharField(max_length=80, null=False)
#     last_updated_datetime = models.DateTimeField(auto_now=True, null=False)
#
#     objects = models.QuerySet()
#
#     class Meta:
#         verbose_name_plural = "ClustersDetails"


class ContentTypes(models.Model):
    """
       10 CONTENT TYPES TABLE
    """
    content_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # catalogue_type_name: Food, Health, Fashion, News, Sports, Movies, books, events etc.
    content_type_name = models.CharField(max_length=50, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.content_type_id + " - " + self.content_type_name

    class Meta:
        verbose_name_plural = "ContentTypes"


class ContentsSetupDataContract(models.Model):
    """
       11 CONTENTS SETUP, DATA AND CONTRACT TABLE
    """
    content_setup_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content_type = models.ForeignKey(ContentTypes, on_delete=models.PROTECT, null=False,
                                     related_name='ContentsSetupDataContract',
                                     related_query_name='ContentSetupDataContract')

    content_title = models.CharField(max_length=128, null=False)
    is_content_new = models.CharField(max_length=4, null=False)

    # Actual data (Image preferably) or directory
    content_data = models.FileField(upload_to='contentsData/', verbose_name="", null=False)

    # Contract related
    client = models.ForeignKey('ClientsProfile', on_delete=models.PROTECT, null=False,
                               related_name='ContentsSetupDataContract', related_query_name='ContentSetupDataContract')
    our_representative = models.ForeignKey('EmployeesProfile', on_delete=models.CASCADE, null=False,
                                           related_name='ContentsSetupDataContract',
                                           related_query_name='ContentSetupDataContract')

    # Actual data (PDF preferably) or directory. Note: File name (client_id + content_contract_id)
    content_contract_data = models.FileField(upload_to='contractFile/', verbose_name="", null=False)
    fee_paid = models.DecimalField(max_digits=13, decimal_places=2, null=False)

    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.content_setup_id + " - " + self.content_title

    class Meta:
        verbose_name_plural = "ContentsSetupDataContract"


# class ContentsData(models.Model):
#     """
#        12 CONTENTS DATA TABLE
#     """
#     content_data_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     content_setup = models.ForeignKey(ContentsSetup, on_delete=models.PROTECT, null=False, related_name='contentsData',
#                                       related_query_name='contentData')
#     # Actual data (Image preferably) or directory
#     content_data = models.FileField(upload_to='contentsData/', verbose_name="", null=False)
#
#     last_modified_user = models.CharField(max_length=80, null=False)
#     last_updated_datetime = models.DateTimeField(auto_now=True, null=False)
#
#     objects = models.QuerySet()
#
#     def __str__(self):
#         return self.content_data_id + " - " + self.content_setup.content_title
#
#     class Meta:
#         verbose_name_plural = "ContentsData"
#

class ClientsProfile(models.Model):
    """
       13 CLIENT PROFILE TABLE
    """
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=100, null=False)
    client_tel = models.CharField(max_length=12, null=False)
    client_email = models.EmailField(max_length=100, null=False)
    client_address = models.CharField(max_length=100, null=False)
    contact_person = models.CharField(max_length=50, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.client_id + " - " + self.client_name

    class Meta:
        verbose_name_plural = "ClientsProfile"


# class ContentContracts(models.Model):
#     """
#        14 CONTENTS CONTRACTS TABLE
#     """
#     content_contract_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     content_setup = models.ForeignKey(ContentsSetup, on_delete=models.PROTECT, null=False,
#                                       related_name='contentContracts',
#                                       related_query_name='contentContract')
#     client = models.ForeignKey(ClientsProfile, on_delete=models.PROTECT, null=False, related_name='contentContracts',
#                                related_query_name='contentContract')
#     our_representative = models.ForeignKey('EmployeesProfile', on_delete=models.CASCADE, null=False,
#                                            related_name='contentContracts', related_query_name='contentContract')
#
#     # Actual data (PDF preferably) or directory. Note: File name (client_id + content_contract_id)
#     content_contract_data = models.FileField(max_length=128, null=False)
#     fee_paid = models.DecimalField(max_digits=13, decimal_places=2, null=False)
#
#     start_date = models.DateField(null=False)
#     end_date = models.DateField(null=False)
#
#     last_modified_user = models.CharField(max_length=80, null=False)
#     last_updated_datetime = models.DateTimeField(auto_now=True, null=False)
#
#     objects = models.QuerySet()
#
#     def __str__(self):
#         return self.content_contract_id + " - " + self.client.client_name
#
#     class Meta:
#         verbose_name_plural = "ContentContracts"


class ActiveClustersAndDevices(models.Model):
    """
       15 ACTIVE CLUSTERS AND DEVICES TABLE
    """
    active_cluster_and_device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_setup = models.ForeignKey(ClustersSetup, on_delete=models.PROTECT, null=False,
                                      related_name='ActiveClustersAndDevices',
                                      related_query_name='ActiveClusterAndDevice')
    device = models.ForeignKey(Devices, on_delete=models.PROTECT, null=False, related_name='ActiveClustersAndDevices',
                               related_query_name='ActiveClusterAndDevice')

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.active_cluster_and_device_id

    class Meta:
        verbose_name_plural = "ActiveClustersAndDevices"


class ActiveClustersAndContents(models.Model):
    """
       15 ACTIVE CLUSTERS AND CONTENT DISPLAY TABLE
    """
    active_cluster_and_content_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_setup = models.ForeignKey(ClustersSetup, on_delete=models.PROTECT, null=False,
                                      related_name='ActiveClustersAndContents',
                                      related_query_name='ActiveClusterAndContent')
    content_setup = models.ForeignKey(ContentsSetupDataContract, on_delete=models.PROTECT, null=False,
                                      related_name='ActiveClustersAndContents',
                                      related_query_name='activeClusterAndContent')

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.active_cluster_and_content_id

    class Meta:
        verbose_name_plural = "ActiveClustersAndContents"


class EmployeesProfile(models.Model):
    """
       16 EMPLOYEES PROFILE TABLE
    """
    employee_id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4, editable=False)
    employee_lname = models.CharField(max_length=100, null=False)
    employee_fname = models.CharField(max_length=100, null=False)
    employee_tel = models.CharField(max_length=12, null=False)
    employee_oemail = models.EmailField(max_length=100, null=False)
    employee_pemail = models.EmailField(max_length=100, null=False)
    employee_address = models.CharField(max_length=100, null=False)
    personal_tel = models.CharField(max_length=12, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True, null=False)

    objects = models.QuerySet()

    def __str__(self):
        return self.employee_id + " - " + self.employee_fname

    class Meta:
        verbose_name_plural = "EmployeesProfile"


class StaffLogin(models.Model):
    """
        17 STAFF LOGIN TABLE
    """
    staff_login_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(EmployeesProfile, on_delete=models.PROTECT, null=False, related_name='staffLogins',
                                 related_query_name='staffLogin')
    login_password = models.CharField(max_length=128, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True)

    objects = models.QuerySet()

    def __str__(self):
        return self.staff_login_id + " - " + self.employee.employee_oemail

    class Meta:
        verbose_name_plural = "StaffLogin"


class ClientsLogin(models.Model):
    """
        18 CLIENTS LOGIN TABLE
    """
    client_login_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(ClientsProfile, on_delete=models.PROTECT, null=False)
    login_password = models.CharField(max_length=128, null=False)

    last_modified_user = models.CharField(max_length=80, null=False)
    last_updated_datetime = models.DateTimeField(auto_now=True)

    objects = models.QuerySet()

    def __str__(self):
        return self.client_login_id + " - " + self.client.client_name

    class Meta:
        verbose_name_plural = "ClientsLogin"


class ChangeRequest(models.Model):
    """
        19 CHANGE REQUEST
    """
    change_request_id = models.AutoField(primary_key=True, editable=False)
    change_request_title = models.CharField(max_length=64, null=False)
    change_request_message = models.CharField(max_length=512, null=False)


class Test(models.Model):
    test_id = models.AutoField(primary_key=True, editable=False)
    content_title = models.CharField(max_length=128, null=False)
    content_data = models.FileField(upload_to='contentsDataTest/', null=True, verbose_name="")

    objects = models.QuerySet()

    def __str__(self):
        return self.content_title + ": " + str(self.content_data)
