*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  
    ...    Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  kalle1
    Set Password  kalle12
    Set Password Confirmation  kalle12
    Click Button  Register
    Register Should Fail With Message  
    ...    Password should be at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle2
    Set Password  kalleeee
    Set Password Confirmation  kalleeee
    Click Button  Register
    Register Should Fail With Message  
    ...    Password should not contain only alphabets

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle1
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Click Button  Register
    Register Should Fail With Message  
    ...    Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle0
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  
    ...    User with username kalle0 already exists

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle0  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

