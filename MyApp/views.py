from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Contact
from .forms import ContactForm

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    # or  success_url ="/contact/add"
    success_url = reverse_lazy('contact-list')
    
class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'   
    
class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_delete.html'
    success_url = reverse_lazy('contact-list')     
    
class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_update.html'
    success_url = reverse_lazy('contact-list')    
    
    
    
    
    
    
    