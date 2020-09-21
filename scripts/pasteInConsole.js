let videoLinks = [];

while (document.querySelector('.jsx-1169024735.control-icon.arrow-right')) {
    document.querySelector('.jsx-1169024735.control-icon.arrow-right').click();
    videoLinks.push(window.location.href);
};

console.log(videoLinks);
