import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

""" CONFIGURATIONS -----------------------------------------------------------------------------------------------"""

AUTH_USER_MODEL = 'accounts.User'
ROOT_URLCONF = 'cocognite.urls'
WSGI_APPLICATION = 'cocognite.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
SECRET_KEY = "12367812790631263092183712-37123"

DEBUG = True
SERVER = False
TEST = False
ALLOWED_HOSTS = ['*']
SITE_ID = 1

if TEST:
    SITE_ID = 2

if SERVER:
    SITE_ID = 3

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = '/accounts/cross-auth/'

""" INSTALLATIONS ------------------------------------------------------------------------------------------------"""

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REQUIRED_APPLICATIONS
    'crispy_forms',
    'ckeditor',

    # AUTH_API
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # USER_APPLICATIONS
    'src.accounts',
    'src.website',

    'src.portals.customer',
    'src.portals.admins',

    # MUST BE AT THE END
]

""" SECURITY AND MIDDLEWARES -------------------------------------------------------------------------------------"""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

""" TEMPLATES AND DATABASES -------------------------------------------------------------------------------------- """
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


def load_model_(list_strings):
    print('predicting')
    try:
        list_words = predict_audio_transcription(list_strings).split()
        return concatenate(list_words)
    except:
        return []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

""" INTERNATIONALIZATION ----------------------------------------------------------------------------------------- """

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True

""" PATHS STATIC AND MEDIA --------------------------------------------------------------------------------------- """

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

""" EMAIL AND ALL AUTH ------------------------------------------------------------------------------------------- """

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'donald.duck0762@gmail.com'
EMAIL_HOST_PASSWORD = 'ybwchppsknpddabc'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'CORE-Team <noreply@core.com>'

SOCIALACCOUNT_PROVIDERS = {
    'google': {'SCOPE': ['profile', 'email', ],
               'AUTH_PARAMS': {'access_type': 'online', }}
}

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()


def concatenate(list_strings):
    import time
    str_ = ''
    for string in list_strings:
        if any(string in s for s in DATASET.split()):
            time.sleep(0.7)
            print(string)
            str_ += f'{string} '
    return str_


def predict_audio_transcription(path):
    sound = AudioSegment.from_wav(path)
    chunks = split_on_silence(sound,
                              min_silence_len=500,
                              silence_thresh=sound.dBFS - 14,
                              keep_silence=500, )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError:
                pass
            else:
                text = f"{text.capitalize()}. "
                whole_text += concatenate(text.split())
        print(x if i % 3 == 0 else '')
    return whole_text


DATASET = """
ability
able
about
above
accept
according
account
across
act
action
activity
actually
add
address
administration
admit
adult
affect
after
again
against
age
agency
agent
ago
agree
agreement
ahead
air
all
allow
almost
alone
along
already
also
although
always
American
among
amount
analysis
and
animal
another
answer
any
anyone
anything
appear
apply
approach
area
argue
arm
around
arrive
art
article
artist
as
ask
assume
at
attack
attention
attorney
audience
author
authority
available
avoid
away
baby
back
bad
bag
ball
bank
bar
base
be
beat
beautiful
because
become
bed
before
begin
behavior
behind
believe
benefit
best
better
between
beyond
big
bill
billion
bit
black
blood
blue
board
body
book
born
both
box
boy
break
bring
brother
budget
build
building
business
but
buy
by
call
camera
campaign
can
cancer
candidate
capital
car
card
care
career
carry
case
catch
cause
cell
center
central
century
certain
certainly
chair
challenge
chance
change
character
charge
check
child
choice
choose
church
citizen
city
civil
claim
class
clear
clearly
close
coach
cold
collection
college
color
come
commercial
common
community
company
compare
computer
concern
condition
conference
Congress
consider
consumer
contain
continue
control
cost
could
country
couple
course
court
cover
create
crime
cultural
culture
cup
current
customer
cut
dark
data
daughter
day
dead
deal
death
debate
decade
decide
decision
deep
defense
degree
Democrat
democratic
describe
design
despite
detail
determine
develop
development
die
difference
different
difficult
dinner
direction
director
discover
discuss
discussion
disease
do
doctor
dog
door
down
draw
dream
drive
drop
drug
during
each
early
east
easy
eat
economic
economy
edge
education
effect
effort
eight
either
election
else
employee
end
energy
enjoy
enough
enter
entire
environment
environmental
especially
establish
even
evening
event
ever
every
everybody
everyone
everything
evidence
exactly
example
executive
exist
expect
experience
expert
explain
eye
face
fact
factor
fail
fall
family
far
fast
father
fear
federal
feel
feeling
few
field
fight
figure
fill
film
final
finally
financial
find
fine
finger
finish
fire
firm
first
fish
five
floor
fly
focus
follow
food
foot
for
force
foreign
forget
form
former
forward
four
free
friend
from
front
full
fund
future
game
garden
gas
general
generation
get
girl
give
glass
go
goal
good
government
great
green
ground
group
grow
growth
guess
gun
guy
hair
half
hand
hang
happen
happy
hard
have
he
head
health
hear
heart
heat
heavy
help
her
here
herself
high
him
himself
his
history
hit
hold
home
hope
hospital
hot
hotel
hour
house
how
however
huge
human
hundred
husband
I
idea
identify
if
image
imagine
impact
important
improve
in
include
including
increase
indeed
indicate
individual
industry
information
inside
instead
institution
interest
interesting
international
interview
into
investment
involve
issue
it
item
its
itself
job
join
just
keep
key
kid
kill
kind
kitchen
know
knowledge
land
language
large
last
late
later
laugh
law
lawyer
lay
lead
leader
learn
least
leave
left
leg
legal
less
let
letter
level
lie
life
light
like
likely
line
list
listen
little
live
local
long
look
lose
loss
lot
love
low
machine
magazine
main
maintain
major
majority
make
man
manage
management
manager
many
market
marriage
material
matter
may
maybe
me
mean
measure
media
medical
meet
meeting
member
memory
mention
message
method
middle
might
military
million
mind
minute
miss
mission
model
modern
moment
money
month
more
morning
most
mother
mouth
move
movement
movie
Mr
Mrs
much
music
must
my
myself
name
nation
national
natural
nature
near
nearly
necessary
need
network
never
new
news
newspaper
next
nice
night
no
none
nor
north
not
note
nothing
notice
now
n't
number
occur
of
off
offer
office
officer
official
often
oh
oil
ok
old
on
once
one
only
onto
open
operation
opportunity
option
or
order
organization
other
others
our
out
outside
over
own
owner
page
pain
painting
paper
parent
part
participant
particular
particularly
partner
party
pass
past
patient
pattern
pay
peace
people
per
perform
performance
perhaps
period
person
personal
phone
physical
pick
picture
piece
place
plan
plant
play
player
PM
point
police
policy
political
politics
poor
popular
population
position
positive
possible
power
practice
prepare
present
president
pressure
pretty
prevent
price
private
probably
problem
process
produce
product
production
professional
professor
program
project
property
protect
prove
provide
public
pull
purpose
push
put
quality
question
quickly
quite
race
radio
raise
range
rate
rather
reach
read
ready
real
reality
realize
really
reason
receive
recent
recently
recognize
record
red
reduce
reflect
region
relate
relationship
religious
remain
remember
remove
report
represent
Republican
require
research
resource
respond
response
responsibility
rest
result
return
reveal
rich
right
rise
risk
road
rock
role
room
rule
run
safe
same
save
say
scene
school
science
scientist
score
sea
season
seat
second
section
security
see
seek
seem
sell
send
senior
sense
series
serious
serve
service
set
seven
several
sex
sexual
shake
share
she
shoot
short
shot
should
shoulder
show
side
sign
significant
similar
simple
simply
since
sing
single
sister
sit
site
situation
six
size
skill
skin
small
smile
so
social
society
soldier
some
somebody
someone
something
sometimes
son
song
soon
sort
sound
source
south
southern
space
speak
special
specific
speech
spend
sport
spring
staff
stage
stand
standard
star
start
state
statement
station
stay
step
still
stock
stop
store
story
strategy
street
strong
structure
student
study
stuff
style
subject
success
successful
such
suddenly
suffer
suggest
summer
support
sure
surface
system
table
take
talk
task
tax
teach
teacher
team
technology
television
tell
ten
tend
term
test
than
thank
that
the
their
them
themselves
then
theory
there
these
they
thing
think
third
this
those
though
thought
thousand
threat
three
through
throughout
throw
thus
time
to
today
together
tonight
too
top
total
tough
toward
town
trade
traditional
training
travel
treat
treatment
tree
trial
trip
trouble
true
truth
try
turn
TV
two
type
under
understand
unit
until
up
upon
us
use
usually
value
various
very
victim
view
violence
visit
voice
vote
wait
walk
wall
want
war
watch
water
way
we
weapon
wear
week
weight
well
west
western
what
whatever
when
where
whether
which
while
white
who
whole
whom
whose
why
wide
wife
will
win
wind
window
wish
with
within
without
woman
wonder
word
work
worker
world
worry
would
write
writer
wrong
yard
yeah
year
yes
yet
you
young
your
yourself
"""
x = """
WARNING:tensorflow:6 out of the last 6 calls to <function Model.make_predict_function.<locals>.predict_function at 0x0000021C42328430> triggered tf.function retracing. Tracing is expensive and the excessive number of tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing tensors with different shapes, (3) passing Python objects instead of tensors. For (1), please define your @tf.function outside of the loop. For (2), @tf.function has experimental_relax_shapes=True option that relaxes argument shapes that can avoid unnecessary retracing. For (3), please refer to https://www.tensorflow.org/guide/function#controlling_retracing and https://www.tensorflow.org/api_docs/python/tf/function for  more details."""
