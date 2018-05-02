from django.db import models

class ConverterEquation(models.Model):
    """
    Model representing SMPS converter equation
    """
    name = models.CharField(max_length=200, help_text="Enter the name of this converter in the admin page.")
    
    input_output_transfer = models.TextField(max_length=5000, help_text="Enter the input to output transfer function of the converter.")
    input_impedance = models.TextField(max_length=5000, help_text="Enter the input impedance of the converter.")
    output_impedance = models.TextField(max_length=5000, help_text="Enter the output impedance of the converter.")
    duty_output_transfer = models.TextField(max_length=5000, help_text="Enter the duty to output transfer function of the converter.")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
    def get_absolute_url(self):
        """
        Returns the url to access.
        """
        pass

    def get_in_out_transfer(self):
        """
        Returns the input to output transfer function.
        """
        return self.input_output_transfer
    
    def get_input_impedance(self):
        """
        Returns the input impedance transfer function.
        """
        return self.input_impedance

    def get_output_impedance(self):
        """
        Returns the output impedance transfer function.
        """
        return self.output_impedance
    
    def get_duty_output_transfer(self):
        """
        Returns the duty cycle to output transfer function.
        """
        return self.duty_output_transfer