const admin = require('firebase-admin')
const functions = require('firebase-functions');

admin.initializeApp(functions.config().firebase)

function saveNewUserToDatabase(ev => {
  const user = event.data;
  const email = user.email;
  const uid = user.uid;
  const displayName = user.displayName;

  console.log('Registering: user, email: ', user, email);
})

exports.registerEveryNewUserInDatabase = functions.auth.user().onCreate(saveNewUserToDatabase);
