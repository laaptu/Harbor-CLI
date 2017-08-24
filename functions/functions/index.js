const admin = require('firebase-admin')
const functions = require('firebase-functions');

admin.initializeApp(functions.config().firebase)

/*
 * Top level functions.
 */
const db = admin.database();

/**
 * Save details of each new user to the database.
 *
 * @param {event} event
 */
function saveNewUserToDatabase(event) {
  const user = event.data;
  const email = user.email;
  const uid = user.uid;

  // Cannot use  email id as a key
  const ref = db.ref('users/' + uid);

  console.log('Registering: user, email: ', uid, email);

  const data = {
    uid: uid,
    email: email,
  };

  ref.set(data);

  console.log('Registeration successful', uid, email);
}

/**
 * On each project release.
 *
 * @param {event} event
 */
function onProjectRelease(event) {
  const project_id = event.params.proj_id;
  const upload_id = event.params.upload_id;

  console.log('project_id "', project_id, '" was released with upload id: . ', upload_id);

  const path = `/members/${project_id}`;
  console.log('path = ', path)

  admin.database().ref(path).once('value', function(snap) {
    const userIds = Object.keys(snap.val());

    for (let userId of userIds) {
      let userTokensPath = `/users/${userId}`;
      admin.database().ref(userTokensPath).once('value', function(snap) {
        let userDetails = snap.val();
        console.log('userDetail : ', userDetails);

        if (!userDetails.fcmTokens) {
          console.log('skipping for: ', userId);
          return;
        }

        let fcmTokensForUser = Object.keys(userDetails.fcmTokens);

        const payload = {
          notification: {
            title: `A new update for ${project_id} is available.`,
          }
        };

        for (let token of fcmTokensForUser) {
          admin.messaging().sendToDevice(token, payload)
            .then(function(response) {
              // See the MessagingDevicesResponse reference documentation for
              // the contents of response.
              console.log("Successfully sent message:", response);
            })
            .catch(function(error) {
              console.log("Error sending message:", error);
            });
        }

      });
    }

  });
}

exports.registerEveryNewUserInDatabase = functions.auth.user().onCreate(saveNewUserToDatabase);
exports.onProjectRelease = functions.database.ref('/projects/{proj_id}/uploads/{upload_id}').onWrite(onProjectRelease);
