import sys
sys.path.insert(0,'../')
from ExtraDriver import attachMate,extradriver
from test.screens.screens import As400MainMenu,screenLoggin
from behave import *

session=None
Juan=None

@given(u'The Extra client is already open on {Session}')
def step_impl(context,Session):
    global session
    session=attachMate().OpenExtraSession(f'../Session1.EDP')
    session=attachMate().getActiveSession()
    global Juan
    Juan=extradriver(session)
    

@given(u'Juan is already logged on pub400 server with {Username} and {Password}')
def step_impl(context,Username,Password):

    Juan.writeOn(screenLoggin['User'],Username)
    Juan.writeOn(screenLoggin['Password'],Password)
    Juan.GoToNextScreen()


@when(u'Juan go to the Display Job Attributes Screen')
def step_impl(context):
    Juan.writeOn(As400MainMenu['Command'],'3')
    Juan.GoToNextScreen()
    Juan.writeOn(As400MainMenu['Command'],'1')
    Juan.GoToNextScreen()
    Juan.writeOn(As400MainMenu['Command'],'7')
    Juan.GoToNextScreen()


@then(u'Juan should the {Username} as Job user indentity')
def step_impl(context,Username):
    Juan.writeOn('Command to run . . . . . . . . . CMD',Username + ' Ttextexto texto ')
    Juan.writeOn('Job name','campo1')
    Juan.writeOn('Job description','campo2')
    Juan.writeOn('Job priority','campo3')
    Juan.writeOn('Print device','campo4')




