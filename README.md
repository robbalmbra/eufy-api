# eufy-api
Looking into the eufy android apk, I found references to different API calls and how to authenticate to eufy for different services.

# Authentication

Using the API call, a user can authenticate to eufy. Fill in the email and password fields with the credentials used for eufy.

```
curl --location 'https://home-api.eufylife.com/v1/user/v2/email/login' \
--header 'category: Health' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "eufy-app",
    "client_secret":"8FHf22gaTKu7MZXqz5zytw",
    "email":"",
    "password":""
}'
```

Once run, the command will return metadata associated with the account including the fields `access_token` and `refresh_token` that can be used for other API calls.

# Example
Using the access token within the example request, we can retrieve a list of devices associated with the account:

```
curl --location 'https://home-api.eufylife.com/v1/device/' \
--header 'token: <ACCESS_TOKEN>'
```

The python file [example.py](example.py) contains a class and methods to authenticate and pull information about devices.

# API Calls

Calls extracted from eufylife apk.

| Method | URL | Description |
|--------|-----|-------------|
| DELETE | calorie/intake_item/{id} | deleteCaloriesIntake |
| DELETE | caring/content/favorite/{content_id} | deleteCaringContentFavorite |
| DELETE | device/data/{deviceId}/{customerId} | deleteAllHistory |
| DELETE | device/wifi_scale/{deviceId} | unBindWifiScale |
| DELETE | device/{deviceId} | deleteDevice |
| DELETE | device/{deviceId}/data/{id} | deleteOneHistory |
| DELETE | device/{device_id} | deleteDevice |
| DELETE | food/{code} | deleteCustomFood |
| DELETE | genie/remove_genie/{deviceId} | removeGenie |
| DELETE | genie/sign_out_alexa/{deviceId} | signOutFromAmazon |
| DELETE | notification/delete_all | deleteAllNotification |
| DELETE | notification/{notificationId}/delete | deleteSingleNotification |
| DELETE | user/customer/{id} | deleteMember |
| DELETE | user/destroy | destroyUser |
| DELETE | voice_pkg/delete | deleteVoicePack |
| GET | advertisement/close/{advertiseID} | saveAdvertToNotice |
| GET | advertisement/life | getAdvertisement |
| GET | away/{deviceId}/get-timer | getAwayModeTimer |
| GET | body_model/ | gatHumanModelData |
| GET | body_model/ | gatHumanModelLimitData |
| GET | body_model/data_day | getHumanModelDateList |
| GET | calorie/ | getCaloriesByDate |
| GET | calorie/data_day | getCaloriesValidDate |
| GET | calorie/like_food | getCaloriesLikeFood |
| GET | caring/activity | getCaringActivity |
| GET | caring/content | getCaringOperationContent |
| GET | caring/homepage/content | getCaringContent |
| GET | caring/upgrade_product | getUpgradeList |
| GET | caring/upgrade_product/new_code/{code} | getNewUpgradeCode |
| GET | caring/upgrade_product/{upgrade_id} | getUpgradeCode |
| GET | customer/all_target | getAllMemberTargetInfo |
| GET | customer/target/{customerID} | getTargetInfo |
| GET | device/ | getDeviceList |
| GET | device/ | getAllDevices |
| GET | device/cleanrecord/{deviceId}/data | getDeviceCleanRecordStatus |
| GET | device/data | getDataHistory |
| GET | device/data/feedback/{dataid} | getFeedBackData |
| GET | device/firmware/{deviceId}/BLE/update/0.0.0 | getDeviceFirmwareInfoByBLE |
| GET | device/firmware/{deviceId}/MCU/update/0.0.0 | getDeviceFirmwareInfoByMCU |
| GET | device/firmware/{deviceId}/RES/update/0.0.0 | getDeviceFirmwareInfoByRES |
| GET | device/last_device_data | getAllUserHistoryData |
| GET | device/setting/{deviceId} | getDeviceSetting |
| GET | device/update/all_components/{device_id} | checkDeviceUpdate |
| GET | device/update/firmware_history/{device_id} | getDeviceFirmwareHistory |
| GET | device/v2 | getDeviceAndGroupsV2 |
| GET | device/wifi_scale/certificate | getWifiScaleCertificate |
| GET | device/wifi_scale/raw_data/{deviceId} | getWifiScaleHistory |
| GET | device/wifi_scale/screen | getDeviceScreen |
| GET | device/wifi_scale/unmatched_data | getWifiScaleAbnormalDataList |
| GET | device/wifi_scale/version/{deviceId} | checkOtaVersion |
| GET | device/{deviceId}/data | getHistory |
| GET | energy/{deviceId}/get-today | getTodayData |
| GET | energy/{deviceId}/get-total-electric | getTotalElectricity |
| GET | energy/{deviceId}/get-total-runtime | getTotalRuntime |
| GET | food/ | searchCustomFood |
| GET | genie/get_avs_product/{deviceId} | getAvsProduct |
| GET | genie/get_languages/{productCode} | getGenieLanguage |
| GET | help/faq/{productCode} | getFaq |
| GET | help/faq/{product_code} | getDeviceFaq |
| GET | help/privacy_and_terms | getPrivacy |
| GET | help/third_party | getSmartIntegrationsUrls |
| GET | help/v2/faqs/evaluation/{faqID} | getFAQEvaluation |
| GET | help/v2/faqs/{productCode} | getDeviceFaqV2 |
| GET | help/v2/resource/language/{productCode}/{type} | getDeviceHelpManualLanguageList |
| GET | help/v2/resource/{productCode} | getDeviceHelpResource |
| GET | help/v2/upload_url | getUploadUrl |
| GET | help/website | getEufyWebsite |
| GET | lefu/food/foodSearchAll | foodSearchForeign |
| GET | lefu/food/getDetail | getFoodDetailsForeign |
| GET | notification/get | requestNotificationsPaginationList |
| GET | notification/get/home | requestMessagesHomeData |
| GET | notification/get/v2 | requestMessagesPaginationList |
| GET | notification/get_all | requestNotificationsList |
| GET | notification/life | requestNotificationsPaginationList |
| GET | product/appliances/all_region | fetchProducts |
| GET | rating/get_rating | getIfPopAppRating |
| GET | rating/get_rating | getRating |
| GET | reddot/life | getMainMenuRedDot |
| GET | reddot/v2 | getExploreReddot |
| GET | reminder/ | getReminder |
| GET | report/month | getReportMonthList |
| GET | report/month/{id} | getReportMonthById |
| GET | report/week | getReportWeekList |
| GET | report/week/is_gen | getReportWeekDataState |
| GET | report/week/{id} | getReportWeekById |
| GET | resource/voicePackage | getVoicePackage |
| GET | share/active/list_device_share | getDeviceShare |
| GET | share/active/single_device_share/{deviceId} | requestShareList |
| GET | survey/list | questionList |
| GET | survey/reddot | questionRedDot |
| GET | target_question/ | getGoalQuestion |
| GET | user/app/upload_url | getUploadLogUrl |
| GET | user/customers | getMembers |
| GET | user/details | getUserDetail |
| GET | user/email/registered | registered |
| GET | user/password/forget | forgotPassword |
| GET | user/user_center_info | updateUserCenterToken |
| GET | user/user_center_token | getUserCenterToken |
| GET | user/wifi_scale/expired_devices | getUserExpiredDevice |
| GET | voice_pkg/status | voicePackComposeState |
| GET | voice_pkg/support_lang | voicePackSupportLanguage |
| POST | /push_log_es | pushLogES |
| POST | /push_log_hdfs | pushLogHdfs |
| POST | away/save-timer | saveAwayModeTimer |
| POST | away/stop-timer | stopAwayModeTimer |
| POST | body_model | updateHumanModel |
| POST | body_model/ | addHumanModel |
| POST | calorie/ | addCalories |
| POST | calorie/burn_item | addCaloriesBurn |
| POST | calorie/copy_data | copyCalories |
| POST | calorie/intake_item | addCaloriesIntake |
| POST | calorie/like_food | updateCaloriesLikeFood |
| POST | caring/content/favorite/{content_id} | setCaringContentFavorite |
| POST | customer/target/{customerID} | upDateTargetInfo |
| POST | device | saveDeviceName |
| POST | device/ | updateDevice |
| POST | device/bulkData | postWifiScaleHistory |
| POST | device/bulkData | postHistory |
| POST | device/data/unmatched_data | postWifiScaleAbnormalData |
| POST | device/hardware_version | setHardWareVersion |
| POST | device/report/upgrade_result | uploadUpgradeDeviceFirmwareResult |
| POST | device/report/upgrade_start | upgradeStart |
| POST | device/reset_wifi | resetWifi |
| POST | device/send_device_data | sendDeviceDataToEmail |
| POST | device/setting | postDeviceSetting |
| POST | device/setting/el | updateDeviceUnit |
| POST | device/setting/el | updateDeviceSetting |
| POST | device/setup/wifi_setup_confirm | bindWifiDevice |
| POST | device/wifi_scale/bulkData | distributeWifiScaleAbnormalData |
| POST | device/wifi_scale/screen | setDeviceScreen |
| POST | device/wifi_scale/version | uploadWifiScaleVersion |
| POST | energy/clear-data | clearData |
| POST | food/ | addCustomFood |
| POST | genie/check_wifi_setup | genieBindDevice |
| POST | genie/save_upgrade_setting | upgradeSetting |
| POST | genie/send_alexa_token | sendAlexaTokenToServer |
| POST | genie/update_genie | updateGenie |
| POST | help/v2/faqs/evaluation | setFAQEvaluation |
| POST | notification/life/save-push-token | savePushToken |
| POST | notification/mark/{notificationType} | readAllNotificationsByType |
| POST | notification/mark_read | readNotifications |
| POST | notification/save-push-token | savePushToken |
| POST | pop_up/is_need | popAmazonInviteEnable |
| POST | push_log_es | pushLogElectrode |
| POST | push_log_es | pushLogHistory |
| POST | push_log_es | pushLogCreateTime |
| POST | push_log_es | pushLogDeleteHistory |
| POST | push_log_es | pushLogAdvert |
| POST | push_log_hdfs | pushLogElectrodeHDFS |
| POST | rating/record_event | recordEvent |
| POST | rating/record_event | recordRatingEvent |
| POST | reddot/v2/report | exploreReddotReport |
| POST | reminder/ | addReminder |
| POST | report/week | genReportWeek |
| POST | share/active/accept_invitation | acceptOtherShareDevice |
| POST | share/active/deny_invitation | denyOtherShareDevice |
| POST | share/active/fetch_share_of_receiver | fetchDeviceShare |
| POST | share/active/share_device | shareMineDevice |
| POST | tuya/create_group | createGroup |
| POST | user/customer | updateMember |
| POST | user/customer | updateCardOrderMember |
| POST | user/device/upload_url | getDeviceUploadLogUrl |
| POST | user/email/register | register |
| POST | user/email/registered | registered |
| POST | user/info | updateUser |
| POST | user/mobile/forgetPassword | mobileForgetPassword |
| POST | user/mobile/register | mobileRegister |
| POST | user/mobile/verificationCode | getVerificationCode |
| POST | user/password/change | changePassword |
| POST | user/password/reset | mobileResetPassword |
| POST | user/save-home-setting | saveHomeSetting |
| POST | user/v2/email/login/ | login |
| POST | user/v2/mobile/login | mobileLogin |
| POST | user/wifi_scale/bind_code | getWifiScaleCode |
| POST | user/wifi_scale/token | getUserDeviceToken |
| POST | voice_pkg/apply | applyVoicePack |
| POST | voice_pkg/auto_upgrade | autoUpgradeVoicePack |
| POST | voice_pkg/update | updateVoicePack |
| POST | voice_pkg/upload | uploadVoicePack |
| PUT | calorie/intake_item/{id} | updateCaloriesIntake |
| PUT | calorie/{id} | updateCalories |
| PUT | device/cleanrecord/add | uploadCleanRecordStatus |
| PUT | device/data/feedback | addFeedBackData |
| PUT | device/mul | bindDevice |
| PUT | help/feedback/{productCode} | sendFeedback |
| PUT | help/feedback/{product_code} | submitFeedback |
| PUT | help/feedback_directly | submitFeedbackDirectly |
| PUT | help/v2/feedback | submitFeedbackWithPictures |
| PUT | pop_up/change_pop_state | popAmazonInviteLogReport |
| PUT | reminder/{id} | updateReminder |
| PUT | tuya/add_device | uploadTuyaDeivceInfo |
| PUT | user/customer | createMember |

# Todo

* Retrieve payloads for POST methods
* Build out example.py class for other API calls
