//function to save the edited post
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function editPost(postid){
    const content = document.querySelector(`#content_${postid}`).value;
    if (content == ""){
        alert("Please enter some content");
        return;
    }
    console.log("content: " + content);
    console.log("savePost called with postid: " + postid);
    fetch(`/edit/${postid}`, {
        method: 'post',
        headers:{"X-CSRFToken": csrftoken , 'Content-Type': 'application/json'},
        body: JSON.stringify({
            content: content
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log("result: " + result + "result.content: " + result.content);
        const content = document.querySelector(`#content_${postid}`).value ;
        console.log("content: " + content);
        document.querySelector(`#content_${postid}`).value = result.content;
        document.querySelector(`#paracontent_${postid}`).innerHTML = result.content;
    })
}
//function to like a post


function likePost(postid, isauthenticated){
    console.log("likePost called with postid: " + postid + "isauthenticated: " + isauthenticated);
    if (isauthenticated == "False"){
        alert("Please login to like a post");
        return;
    }

    fetch(`/like/${postid}`, {
        method: 'post',
        headers:{"X-CSRFToken": csrftoken , 'Content-Type': 'application/json'},
        body: JSON.stringify({
            postid: postid
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log("result: " + result + "result.likes: " + result.likes);
        document.querySelector(`#like_${postid}`).innerHTML = result.likes;
        div = document.querySelector(`#likePosticon_${postid}`);
        console.log("div: " + div);
        if (result.liked == true){
            div.innerHTML =
            `
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
                </svg>
            `
        }
        else
        {
            div.innerHTML = 
            `
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                            <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
                </svg>
            `
        }
                
    })
}
       
function validatePost( postcontent ){
    console.log("validatePost called");
    postcontent = postcontent.value;
    console.log("postcontent: " + postcontent);
    if (postcontent == ""){
        alert("Please enter some content");
        return false;
    }
    return true;

}




const darkModeToggle = document.getElementById('dark-mode-toggle');
const body = document.body;




