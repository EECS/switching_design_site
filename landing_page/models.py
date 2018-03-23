from django.db import models

class landing_page_header(models.Model):
    """
    Model containing the content of the header for the landing page.
    """
    name = models.CharField(max_length=200, help_text="Enter the text to be placed in the header icon.",
    primary_key=True)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    
    def __unicode__(self):
        """
        String for representing the Model pk (in Admin site etc.)
        """
        return self.pk
        
    def get_absolute_url(self):
        """
        Returns the url to access.
        """
        pass

class landing_page_home(models.Model):
    """
    Model containing the content of the header for the landing page.
    """
    name = models.TextField(max_length=1000, help_text="Enter the text to be placed in the landing page home webpage.", 
    primary_key=True)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    
    def __unicode__(self):
        """
        String for representing the Model pk (in Admin site etc.)
        """
        return self.pk
        
    def get_absolute_url(self):
        """
        Returns the url to access.
        """
        pass

class landing_page_content(models.Model):
    """
    Model containing the content of the header for the landing page.
    """
    name = models.TextField(max_length=1000, help_text="Enter the text to be placed in the landing page content webpage.", 
    primary_key=True)
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    
    def __unicode__(self):
        """
        String for representing the Model pk (in Admin site etc.)
        """
        return self.pk
        
    def get_absolute_url(self):
        """
        Returns the url to access.
        """
        pass
    
