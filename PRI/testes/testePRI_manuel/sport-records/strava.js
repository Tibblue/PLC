var strava = require('strava-v3');
strava.athlete.listActivities({'access_token':'58017a86f3884b77737cb548f06d0247cddb4dc0'},
    function(err,payload,limits) {
        if (!err) {
			var payloadStr = JSON.stringify(payload);
			payloadStr = payloadStr.replace(/(\s*?{\s*?|\s*?,\s*?)(['"])?([a-zA-Z0-9]+)(['"])?:/g, '$1"$3":');
			console.log(payloadStr); 
		} else { 
			console.log(err); 
		}
    });
