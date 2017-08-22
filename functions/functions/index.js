const admin = require('firebase-admin')
const functions = require('firebase-functions');

admin.initializeApp(functions.config().firebase)

/*
 * Top level functions.
*/
const db = admin.database();

function saveNewUserToDatabase(event) {
  const user = event.data;
  const email = user.email;
  const uid = user.uid;

  const ref = db.ref('users/' + uid);

  console.log('Registering: user, email: ', uid, email);

  const data = {
    uid: uid,
    email: email,
  };

  ref.set(data);

  console.log('Registeration successful', user, email);
}

exports.registerEveryNewUserInDatabase = functions.auth.user().onCreate(saveNewUserToDatabase);
