import pytest
import mock
from project import getArtist,getNums,getResponse,dictTransform,toTime
import builtins



def test_getArtist():
    with mock.patch.object(builtins, 'input', lambda _: 'A'):
        assert getArtist() == ('A','A')
    with mock.patch.object(builtins, 'input', lambda _: 'Alan walker'):
        assert getArtist() == ('Alan+walker','Alan walker')
    with mock.patch.object(builtins, 'input', lambda _: 'lana del rey'):
        assert getArtist() == ('lana+del+rey','lana del rey')

def test_getNums():
    with mock.patch.object(builtins, 'input', lambda _: '10'):
        assert getNums() == 10
    with mock.patch.object(builtins, 'input', lambda _: '15'):
        assert getNums() == 15
    with mock.patch.object(builtins, 'input', lambda _: '5'):
        assert getNums() == 5
    with mock.patch.object(builtins, 'input', lambda _: '23'):
        assert getNums() == 23

def test_getResponse():
    assert getResponse("alan+walker","alan walker",1) == {'Move Your Body': [217907, 'https://music.apple.com/us/album/move-your-body-alan-walker-remix/1162482526?i=1162482642&uo=4']}
    assert getResponse("lana+del+rey","lana del rey",5) == {'Summertime Sadness (Lana Del Rey vs. Cedric Gervais)': [412327, 'https://music.apple.com/us/album/summertime-sadness-lana-del-rey-vs-cedric-gervais-cedric/1445314638?i=1445314644&uo=4'], 'Prisoner (feat. Lana Del Rey)': [274956, 'https://music.apple.com/us/album/prisoner-feat-lana-del-rey/1440826239?i=1440826588&uo=4'], 'Young and Beautiful [Lana Del Rey vs. Cedric Gervais]': [227115, 'https://music.apple.com/us/album/young-and-beautiful-lana-del-rey-vs-cedric-gervais/1445314872?i=1445314874&uo=4'], 'Stargirl Interlude (feat. Lana Del Rey)': [111611, 'https://music.apple.com/us/album/stargirl-interlude-feat-lana-del-rey/1440871397?i=1440871932&uo=4'], 'Summertime Sadness': [265502, 'https://music.apple.com/us/album/summertime-sadness/1440811595?i=1440812085&uo=4']}
    assert getResponse("the+weeknd","the weeknd",4) == {'Crew Love (feat. The Weeknd)': [208813, 'https://music.apple.com/us/album/crew-love-feat-the-weeknd/1440642493?i=1440642735&uo=4'], 'Or Nah (feat. The Weeknd, Wiz Khalifa and DJ Mustard) [Remix]': [242983, 'https://music.apple.com/us/album/or-nah-feat-the-weeknd-wiz-khalifa-and-dj-mustard-remix/884361596?i=884361599&uo=4'], 'Remember You (feat. The Weeknd)': [290078, 'https://music.apple.com/us/album/remember-you-feat-the-weeknd/562648250?i=562648267&uo=4'], 'Low Life (feat. The Weeknd)': [313547, 'https://music.apple.com/us/album/low-life-feat-the-weeknd/1081197363?i=1081197914&uo=4']}

def test_toTime():
    assert toTime(60000) == "1:00"
    assert toTime(120235) == "2:00"
    assert toTime(234222) == "3:54"

def test_dictTransform():
    assert dictTransform({"lmao":[60000,"link"]}) == ({"No.":[1],"Songs":["lmao"],"Duration":["1:00"]},["link"])
     