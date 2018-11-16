Feature: As400SystemLogon

    Juan as
    a Pub400 System
    Wants to
    See the job attributes

    Background: The Extra client is already open
        Given The Extra client is already open on <Session>

    Scenario Outline: Get logged using the demo password and any username

    Given Juan is already logged on pub400 server with <User> and <Password>
    When Juan go to the Display Job Attributes Screen
    Then Juan should the <User> as Job user indentity

    Examples: As400Users
        | User | Password | Session |
        |cjpava||Session1.EDP|

