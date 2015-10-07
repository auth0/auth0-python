$(document).ready(function() {
    var widget = new Auth0Widget({
        // All this properties are set on the .env file
        domain: AUTH0_DOMAIN,
        clientID: AUTH0_CLIENT_ID,
        callbackURL: AUTH0_CALLBACK_URL,
        callbackOnLocationHash: false
    });

    $('.btn-login').click(function(e) {
      e.preventDefault();
      widget.signin();
    });
});
