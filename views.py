import inspect
import json
import logging
import os
from pathlib import Path
import pkgutil
import platform
from random import choice, randint, shuffle 
import re
import time

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from .mastery_modules import _1, _2, _3, _4
#from mastery.utilities import utilities as utl

import question_logic as utl # doesn't exist yet
from question_logic.all import * # doesn't exist yet

logging.basicConfig(filename='mastery_question_logger.log', encoding='utf-8', level=logging.ERROR)
logging.disable(logging.INFO)

def populate_question_logic_dict()->dict:
    """ Used by generate_template_question_and_items(module, key)
    """
    # make the path appropriately depending on OS
    if platform.system() == 'Windows':
        RESOURCE_INPUT_QUESTIONS_PATH = '\\resource_input_questions'
    else:
        RESOURCE_INPUT_QUESTIONS_PATH = '/resource_input_questions'
    
    # list the question logic files using imported ql
    pkgpath = os.path.dirname(utl.__file__)
    question_logic_files = [name for _, name, _ in pkgutil.iter_modules([pkgpath + RESOURCE_INPUT_QUESTIONS_PATH])]

    # put all logic files into a dictionary so we can use their logic
    question_logic_dict = {} # populating question logic dictionary
    for file_name in question_logic_files:
        if file_name not in ['all']:
            #print(file_name)
            exec(f"question_logic_dict['{file_name}']={file_name}.logic")
    #print(question_logic_dict)
    return question_logic_dict

def generate_template_question_and_items(module:'object containing questions dict', key:str)->'template_question, items':
    """Used by: 
    RandomModuleView and SpecificModuleView
    Uses populate_question_logic_dict() 
    to return template_question and item used in question templates
    """
    resource_type = 'unknown'
    #try:
    if type(module.questions[key]) == dict:
        question_dict = module.questions[key] #get the dict
        if type(question_dict['type'])==str: # If resource type is just a string, there is only one.
            resource_type=question_dict['type']
        else: # resource type is a list/tuple 
            resource_type=choice(question_dict['type'])# and needs to be selected 
        print('resource_type:',resource_type)
        
        question_logic_dict = populate_question_logic_dict() # line 24ish in this file
        
        template_question, items = question_logic_dict[resource_type](question_dict)

    else:
        # Otherwise, we'd better assume we're using a set of unique question logic and try to use that.
        print('logic type question')# Self contained generating its own question and items.
        resource_type = 'logic'
        template_question, items = module.questions[key]()

    shuffle(items) # item order needs to be randomised
    return template_question, items 
    """
    except Exception as e:
        slashes = '\\\\' if platform.system() == 'Windows' else '/'          
        error_str = f"ERROR with {str(module).split(slashes)[-1][:-5]} {key} ({resource_type} question): {e} {print(traceback.format_exc())}"
        logging.error(error_str)
        logging.error(e)
        
        return None, None
    """

module_object_to_name_dict = {
    _1:'Old Testament', 
    _2:'New Testament', 
    _3:'Book of Mormon', 
    _4:'Doctrine and Covenants',
}


class HomeView(TemplateView):
    template_name = 'mastery/home.html'

class PCEPView(TemplateView):
    template_name='python_institute/pcep.html'

class PCAPView(TemplateView):
    template_name='python_institute/pcap.html'

class PCPP1View(TemplateView):
    template_name='python_institute/pcpp1.html'

class PCPP2View(TemplateView):
    template_name='python_institute/pcpp2.html'

class RandomModuleView(TemplateView):
    modules = () # set this in views
    template_name = 'mastery/multichoice.html'
    
    def get_context_data(self, **kwargs):
        start = time.time() # Timing how long all this takes. We'll stop this timer later
        context = super().get_context_data(**kwargs) # make a context object to mess with.
        # 'modules' is a tuple containing module names passed into the view in urls.py. And we're picking one of them. 
        
        template_question = None
        while template_question is None:
            module = choice(self.modules)
            # Each module contains a dictionary called questions and we're picking one of the questions in that dictionary. 
            key = choice(tuple(module.questions.keys()))#from module, get key
            
            slashes = '\\\\' if platform.system() == 'Windows' else '/'# if running in windows, split with \\
            module_str=str(module).split(slashes)[-1][:-5] # and assuming anything else is Linux / 
            
            print(str(module)) # the only way we know what the module is
            print('module_str',module_str) # just checking we have the module code too
            print('key:',key) # and seeing what the key is

            question_type = 'multi-choice' # always multi choice at the moment? Not sure though 10/09/22

            # v Uncomment to use a specific question in a specific module:
            #module = _1
            #key = 'test_question'
            
            template_question, items = generate_template_question_and_items(module, key) # check that below logic matches with function used...
        
        # Put question list and items in context dictionary.
        context['url'] = self.request.path
        context['module'] = module_object_to_name_dict[module]
        context['key'] = key
        context['question'], context['items'] = template_question, items
        context['question_type'] = question_type # Question type may tell the template how to handle the question if needed.
        context['question_description'] = key # Question key, acting as a question description
        context['cert_name'] = re.sub('[0-9]+', '', module_str)# needed in case we switch to specific question
        context['module_name'] = module_object_to_name_dict[module]# question module name needed as above
        context['title'] = 'AWS Cloud Practitioner Practice'# may change later...
        context['question_description_link'] = 'https://duckduckgo.com/?q=aws+' + key.replace('_', '+') # used to link if needed
        # We set this timer at the top so let's stop it now and see how long all that took!
        print('time taken:', time.time()-start)#interesting to know...
        return context

def test_question(request):
    module = e_files_os
    key = 'SQLite3 methods and attributes'
    #callable
    #items, question = module.questions[key]()
    context = {
        'question_type':'multi-choice',
        'items':items, 
        'question':question,
        'key':key,
        }
    return render(request, 'mastery/multichoice.html', context)


#====================#
#for logging feedback#
#====================#
def make_logger(logger_name, logging_filename):
    logger = logging.getLogger(logger_name) # custom logger
    handler = logging.FileHandler(logging_filename) # handler
    handler.setLevel(logging.ERROR)
    custom_format = logging.Formatter('%(asctime)s - %(message)s') # formatting
    handler.setFormatter(custom_format)
    logger.addHandler(handler) # add formatting to handler
    return logger

def log_problem(request):
    # post question details through
    # problem should include module, question key, question text and answer text
    # should get saved to a log
    other = request.POST.get('other')
    problem = request.POST.get('problem') if other == "" else other
    from_url = request.POST.get('url')
    module = request.POST.get('module')
    key = request.POST.get('key')
    question_type = request.POST.get('question_type')
    question = request.POST.get('question')
    
    items = request.POST.get('items')
    items = re.sub('\'', '"', items) # replace ' with " to enable ...
    items = json.loads(items) # str -> list of dicts
    items_str = ''
    for item in items:
        items_str+= ('\n\t'+str(item)) # each dict on a new line tabbed
    
    logger = make_logger('mastery','mastery_question_feedback.log')    
    logger.error(f"{problem}: Module {module}, {key} ({question_type}):\n\t{question}{items_str}")
    
    return HttpResponseRedirect(from_url)
