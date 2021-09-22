
document.querySelectorAll('.video').forEach(function(frame) {
    //get the video link when you hover over a video
    frame.onmouseover = function() {
        const f = frame.firstElementChild;
        const link = f.getAttribute("src"); 
        //console.log(link);
        // send a post request to the server
        fetch('/link', {
        method: 'POST',
        body: JSON.stringify({
            body:link
            
        })
        })
        .then(response => response.json())
        .then(result => {
        var views = result.stats.viewCount;
        var likes = result.stats.likeCount;
        var dislikes = result.stats.dislikeCount;
        var comments = result.stats.commentCount;

        const block = this.nextElementSibling;
        block.style.display='block';
        const v = block.firstElementChild;
        v.innerHTML=`<i class="fas fa-eye"></i>  `+ views;
        const l = v.nextElementSibling;
        l.innerHTML=`<i class="fas fa-thumbs-up" style="color: red;"></i>  `+ likes;
        const d = l.nextElementSibling;
        d.innerHTML=`<i class="fas fa-thumbs-down"style="color: black;"></i>  `+ dislikes;
        const c = d.nextElementSibling;
        c.innerHTML=`<i class="fas fa-comment"></i>  `+ comments;
       // console.log(views, likes, dislikes, comments);
        });
    }
    frame.onmouseout = function() {
        this.nextElementSibling.style.display='none';
      
    }
});

