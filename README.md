<p align="center">
  <img src="https://raw.githubusercontent.com/th3unkn0n/OSI.IG/master/.lib/20191103_233944.jpg" width="300" height="120">
</p>
<p align="center">
</p>
<p align="center"><img src="https://img.shields.io/badge/Version-2.0-brightgreen"></p>
<p align="center">
  <a href="https://github.com/th3unkn0n">
    <img src="https://img.shields.io/github/followers/th3unkn0n?label=Follow&style=social">
  </a>
  <a href="https://github.com/th3unkn0n/osi.ig/stargazers">
    <img src="https://img.shields.io/github/stars/th3unkn0n/osi.ig?style=social">
  </a>
</p>
<p align="center">
  Open Source Information Instagram
</p>

---

so recently ig started sending html response insted of json to "unknown" requests. 

i REALLY wanted this to work without login since i don't use ig anymore, tried few ways i knew to get it working without login but it didn't work :/

<p align="center"><img src="https://c.tenor.com/ujlv7g3-a7QAAAAC/pepo-sad-pepe.gif" width="100" height="100" /></p>

anyways since lot of people are using this i will add a temporary login to get this working asap

---

* The Instagram OSINT Tool gets a range of information from an Instagram account that you normally wouldn't be able to get
from just looking at their profile

* The information includes:

* [ profile ] : user id, followers / following, number of uploads, profile img URL, business enum, external URL, joined Recently, etc

* [ tags & mentions ] : most used hashtags and mentioned accounts

* [ email ] : if any email is used anywhere it'll be displayed

* [ posts ] : accessability caption, location, timestamp, caption, picture url, etc
  * ( yet not working correctly with posts instagram marks as 'sensitive cotent' )  

---

## • How To Install

`$ pkg install -y git`

`$ git clone https://github.com/th3unkn0n/osi.ig.git && cd osi.ig`

`$ python3 -m pip install -r requirements.txt`

## • Usage

`$ python3 main.py -u username`

`$ python3 main.py -h`

`-p, --post images info highlight`


## • Update

`$ git pull`
