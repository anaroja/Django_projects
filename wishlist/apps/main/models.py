# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, postData):
        print postData 
        errors = []
        name = postData['name']
        username = postData['username']
        password = postData['password']
        confirm_password = postData['confirm_password']

        if len(name) is 0:
            errors.append('Name is required')
        elif len(name) < 3:
            errors.append('Name must be at least 3 characters')
        elif not name.isalpha():
            errors.append('Name cannot contain numbers')
        if len(username) is 0:
            errors.append('Username is required')
        elif len(username) < 3:
            errors.append('Username must be at least 3 characters')
        elif not username.isalpha():
            errors.append('Username cannot contain numbers')
        if len(password) is 0:
            errors.append('password is required')
        elif len(password) < 8:
            errors.append('password must be at least 8 characters')
        elif password != confirm_password:
            errors.append('passwords must match')
        
        if len(errors) > 0:
            # show errors to user
            return (False, errors)
        else:
            # first see if that username exists in users table
            result = self.filter(username=username)
            if len(result) > 0:
                # email exists
                errors.append('Username already exists')
                return (False, errors)
            else:
                # username doesn't exist and we can save
                new_user = self.create(
                    name = name,
                    username = username,
                    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                )
                return (True, new_user)
    
    def validate_log(self, postData):
        errors = []
        password = postData['password']
        username = postData['username']
        print postData['password']
        if len(password) is 0:
            errors.append('password is required')
        if len(username) is 0:
            errors.append('Username is required')
        if len(errors) > 0:
            return (False, errors)
        else: 
            # find user by username
            results = self.filter(username=username)
            if len(results) > 0:
                # we found a user with that username
                user = results[0]
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    # successful password
                    return (True, user)
                #password fails
                else:
                    errors.append('Invalid username/Password')
                    return (False, errors)
            else:
                errors.append('Invalid username/Password')
                return (False, errors)


class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    items = models.ManyToManyField(Item, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

