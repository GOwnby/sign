$(document).ready(function() {
    var linkPdfEditor = document.createElement('a');
    var standardLink = '/ManageDocument/Editor/{{ requestID }}';
    var initialLink = standardLink.concat('/no_signatures/none_added');

    linkPdfEditor.setAttribute('href',initialLink);

    document.body.appendChild(linkPdfEditor);

    var countUsersAdded = 0;

    document.querySelector('#add-user').addEventListener('click', function() {
        countUsersAdded = countUsersAdded + 1;

        var userDiv = document.createElement('div');

        var nameDiv = document.createElement('div');
        var emailDiv = document.createElement('div');
        var permissionDiv = document.createElement('div');

        var nameEntry = document.createElement('input');
        nameEntry.setAttribute('type', 'text');
        nameEntry.setAttribute('id', 'name_id_' + countUsersAdded.toString());
        nameEntry.setAttribute('name', 'name_of_user_' + countUsersAdded.toString());
        var nameLabel = document.createElement('label');
        nameLabel.setAttribute('for', 'name_id_' + countUsersAdded.toString());
        nameLabel.innerText('Name:');


        var emailEntry = document.createElement('input');
        emailEntry.setAttribute('type', 'text');
        emailEntry.setAttribute('id', 'email_id_' + countUsersAdded.toString());
        emailEntry.setAttribute('name', 'email_of_user_' + countUsersAdded.toString());
        var emailLabel = document.createElement('label');
        emailLabel.setAttribute('for', 'email_id_' + countUsersAdded.toString());
        emailLabel.innerText('Email:');


        var radioViewPermission = document.createElement('input');
        radioViewPermission.setAttribute('type', 'radio');
        radioViewPermission.setAttribute('id', 'view_permission_' + countUsersAdded.toString());
        radioViewPermission.setAttribute('name', 'permission_user_' + countUsersAdded.toString());
        radioViewPermission.setAttribute('value', 'VIEW');

        var radioViewLabel = document.createElement('label');
        radioViewLabel.setAttribute('for', 'view_permission_' + countUsersAdded.toString());
        radioViewLabel.innerText('View');


        var radioSignPermission = document.createElement('input');
        radioSignPermission.setAttribute('type', 'radio');
        radioSignPermission.setAttribute('id', 'sign_permission_' + countUsersAdded.toString());
        radioSignPermission.setAttribute('name', 'permission_user_' + countUsersAdded.toString());
        radioSignPermission.setAttribute('value', 'SIGN');

        var radioSignLabel = document.createElement('label');
        radioSignLabel.setAttribute('for', 'sign_permission_' + countUsersAdded.toString());
        radioSignLabel.innerText('Sign');


        var radioEditPermission = document.createElement('input');
        radioEditPermission.setAttribute('type', 'radio');
        radioEditPermission.setAttribute('id', 'edit_permission_' + countUsersAdded.toString());
        radioEditPermission.setAttribute('name', 'permission_user_' + countUsersAdded.toString());
        radioEditPermission.setAttribute('value', 'SIGN');

        var radioEditLabel = document.createElement('label');
        radioEditLabel.setAttribute('for', 'edit_permission_' + countUsersAdded.toString());
        radioEditLabel.innerText('Edit');


        nameDiv.appendChild(nameEntry);
        emailDiv.appendChild(emailEntry);

        var indicatePermissions = document.createElement('h3');
        indicatePermissions.innerText('Permission');
        permissionDiv.appendChild(indicatePermissions);
        permissionDiv.appendChild(radioViewPermission);
        permissionDiv.appendChild(radioSignPermission);
        permissionDiv.appendChild(radioEditPermission);

        var finalizeAddUser = document.createElement('button');

        userDiv.appendChild(nameDiv);
        userDiv.appendChild(emailDiv);
        userDiv.appendChild(permissionDiv);
        userDiv.appendChild(finalizeAddUser);

        document.getElementById('users').appendChild(userDiv);

        finalizeAddUser.addEventListener('click', function() {

        });


        linkPdfEditor.setAttribute('href','/ManageDocument/Editor/{{ requestID }}/no_signatures/');
    });
});