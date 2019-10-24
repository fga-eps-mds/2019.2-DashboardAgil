const CLIENT_ID = '1b10677ef95a29f3fdf2 '
const CLIENT_SECRET = '9e57bce3d353b44c84f03af3101daa93a1fbb33a'

const getLoginUrl = (code) =>
    `https://github.com/login/oauth/access_token?client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&code=${code}`

const saveAcessToken = (token) => 
{
    chrome.storage.sync.set({'oauth2_token': token.access_token}, function() 
    {
        console.log('Token salvo')
    })
}

const getAccessToken = (code) => 
{
    fetch(getLoginUrl(code), 
    {
        method: 'POST',
        headers: 
        {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8'
        },
    })
        .then(response => response.json())
        .then(obj => saveAcessToken(obj))
        .catch(error=>console.error(error))
}

const init = () => 
{
    if(location.search.match(/\?code=([\w\/\-]+)/))
    {
        let code = location.search.match(/\?code=([\w\/\-]+)/)[1]
        getAccessToken(code)
    }
}

init()