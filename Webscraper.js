//imports
const {getSubtitles} = require('youtube-captions-scraper');
const fs = require('fs');

//takes in url outputs videoID
function youtube_parser(url){
var regExp = /^.*(youtu\.be\/|vi?\/|u\/\w\/|embed\/|\?vi?=|\&vi?=)([^#\&\?]*).*/;

var match = url.match(regExp);
if (match && match[2].length == 11) {
  return match[2];
} else {
  console.log("URL processing error");
}
}

//urls to test
let urls = ['https://www.youtube.com/watch?v=MAlSjtxy5ak','https://www.youtube.com/watch?v=MAlSjtxy5ak','https://www.youtube.com/watch?v=MAlSjtxy5ak'];
// Fill in youtube Ids here to test


// Fill in youtube Ids here
let youtubeIds = ["xFv_Hl4B83A", 'kyLxTdsT8ws', '_29dz7qDhQk'];

youtubeIds.forEach(async id => {
    let captions = await getSubtitles({videoID: id, lang: 'en'});
    fs.readFile('captions.json', 'utf8', function callback(err, data) {
        if (err) {
            fs.writeFileSync('captions.json', JSON.stringify(captions), 'utf8');
        } else {
        var results = JSON.parse(data);
        results.push(...captions);
        results = JSON.stringify(results);
        fs.writeFileSync('captions.json', results, 'utf8');
        }
    })
});