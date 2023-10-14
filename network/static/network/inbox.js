function savePost(postid){
    const content = document.querySelector(`#content_${postid}`).value; 
    console.log("content: " + content);
    console.log("savePost called with postid: " + postid);
    fetch(`/edit/${postid}`, {
        method: 'post',
        headers:{"X-CSRFToken": '{{ csrf_token }}'},
        body: JSON.stringify({
            content: content
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
        document.querySelector(`#content_${postid}`).value = result.content;
    }
    )
}