.. contents::

Introduction
============

This package provides a new control panel for the Plone content management 
system.  The purpose of this control panel is to allow easy replacement of the
site logo.  

After installing the package, the user will find a new control panel listed in
Plone's Site Setup area. Clicking on the name of the panel will open a view
providing a preview of the current site logo and a file upload field to
replace that logo. If the user chooses to upload a new site logo, that new
logo will replace the existing one, and the logo will change for the site.

Under the hood
==============

The control panel works by creating a new OFS.Image object in the 'custom'
folder of the portal_skins tool. If for some reason, this folder is missing,
the image will be added to the Plone site root. To return to the original,
stock Plone logo, all the user need do is delete this image. Acquisition will
take care of the rest.

