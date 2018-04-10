# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import os
import sys
import subprocess
import uuid
#from Bio import SeqIO
from pprint import pprint, pformat
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from KBaseReport.KBaseReportClient import KBaseReport
#from datetime import datetime

#END_HEADER


class TandemRepeats_landml:
    '''
    Module Name:
    TandemRepeats_landml

    Module Description:
    A KBase module: TandemRepeats_landml
This sample module contains one small method - filter_contigs.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block

    TRF_bin = '/kb/module/TandemRepeats/bin/trf409.linux64'
    # target is a list for collecting log messages
    def log(self, target, message):
        # we should do something better here...
        if target is not None:
            target.append(message)
        print(message)
        sys.stdout.flush()

    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        
        # Any configuration parameters that are important should be parsed and
        # saved in the constructor.
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.scratch = os.path.abspath(config['scratch'])

        #END_CONSTRUCTOR
        pass


    def tandem_repeats(self, ctx, params):
        """
        The actual function is declared using 'funcdef' to specify the name
        and input/return arguments to the function.  For all typical KBase
        Apps that run in the Narrative, your function should have the 
        'authentication required' modifier.
        :param params: instance of type "TandemRepeatsParams" (A 'typedef'
           can also be used to define compound or container objects, like
           lists, maps, and structures.  The standard KBase convention is to
           use structures, as shown here, to define the input and output of
           your function.  Here the input is a reference to the Assembly data
           object, a workspace to save output, and a length threshold for
           filtering. To define lists and maps, use a syntax similar to C++
           templates to indicate the type contained in the list or map.  For
           example: list <string> list_of_strings; mapping <string, int>
           map_of_ints;) -> structure: parameter "assembly_input_ref" of type
           "assembly_ref" (A 'typedef' allows you to provide a more specific
           name for a type.  Built-in primitive types include 'string',
           'int', 'float'.  Here we define a type named assembly_ref to
           indicate a string that should be set to a KBase ID reference to an
           Assembly data object.), parameter "workspace_name" of String,
           parameter "max_period_size" of Long
        :returns: instance of type "TandemRepeatsResults" (Here is the
           definition of the output of the function.  The output can be used
           by other SDK modules which call your code, or the output
           visualizations in the Narrative.  'report_name' and 'report_ref'
           are special output fields- if defined, the Narrative can
           automatically render your Report.) -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN tandem_repeats

        # init
        #
        console = []
        invalid_msgs = []
        self.log(console, 'Running run_TandemRepeats with params=')
        self.log(console, "\n" + pformat(params))
        report = ''

        #### do some basic checks
        #
        if 'workspace_name' not in params:
            raise ValueError('workspace_name parameter is required')
        if 'assembly_input_ref' not in params:
            raise ValueError('assembly_input_ref parameter is required')
        assembly_input_ref = params['assembly_input_ref']

        print('Downloading Assembly data as a Fasta file.')
        assemblyUtil = AssemblyUtil(self.callback_url)
        input_fasta_file = assemblyUtil.get_assembly_as_fasta({'ref': assembly_input_ref})['path']

        print 'PATH: ', input_fasta_file


        # check for necessary files
        if not os.path.isfile(self.TRF_bin):
            raise ValueError("no such file '" + self.TRF_bin + "'")
        if not os.path.isfile(input_fasta_file):
            raise ValueError("no such file '" + input_fasta_file + "'")
        if not os.path.getsize(input_fasta_file) > 0:
            raise ValueError("empty file '" + input_fasta_file + "'")

        # set the output path
#        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
#        output_dir = os.path.join(self.scratch, 'output.' + str(timestamp))
#        if not os.path.exists(output_dir):
#            os.makedirs(output_dir)
#        output_trf_file_path = os.path.join(output_dir, 'tandem_repeats.txt');

        ### Construct the command
        #
        #  e.g. trf yoursequence.txt 2 7 7 80 10 50 500 -f -d -m
        #

        trf_cmd = [self.TRF_bin]
        trf_options = [str(input_fasta_file) ]

        trf_match = 2
        trf_options.append(str(trf_match))
        trf_mismatch = 7
        trf_options.append(str(trf_mismatch))
        trf_delta = 7
        trf_options.append(str(trf_delta))
        trf_pm = 80
        trf_options.append(str(trf_pm))
        trf_pi = 10
        trf_options.append(str(trf_pi))
        trf_minscore = 50
        trf_options.append(str(trf_minscore))
        trf_maxperiod = 500
        trf_options.append(str(trf_maxperiod))
        trf_masked = "-m"
        trf_options.append(trf_masked)
        trf_flank  = "-f"
        trf_options.append(trf_flank)
        trf_data   = "-d"
        trf_options.append(trf_data)
        trf_noredun = "-r"
        trf_maxTR = "-l 2"

        trf_cmd = trf_cmd + trf_options

        # Run Tandem Repeats Finder, capture output as it happens
        #
        self.log(console, 'RUNNING TandemRepeatsFinder:')
        self.log(console, '    ' + ' '.join(trf_cmd))

        #  Runnin TandemRepeatFinder

        p = subprocess.Popen(trf_cmd, \
                             cwd=self.scratch, \
                             shell = False
                            )
        retcode = p.wait()

        self.log(console, 'Returned Contigs: ' + str(p.returncode))
        if p.returncode != 0:
            print "Number of Contigs Analyzed", p.returncode

        # Check that TandemRepeatsFinder produced output
        #
        option_string = '.'.join(trf_options[0:8])
        print os.listdir(self.scratch)
        print "INPUT file = ", input_fasta_file

        html_file =  option_string + ".summary.html"
        mask_file = option_string + ".mask"
        data_file = option_string + ".dat"
        if not os.path.isfile(html_file):
            html_file = option_string + ".1.html"
        if not os.path.isfile(html_file):
            raise ValueError("failed to create TandemRepeats output: " + html_file)
        elif not os.path.getsize(html_file) > 0:
            raise ValueError("created empty file for TandemRepeats output: "+html_file)

        # Upload results
        #
        if len(invalid_msgs) == 0:
            self.log(console,"UPLOADING RESULTS")  # DEBUG

            with open(html_file,'r',0) as html_file_handle:
                html_buf = html_file_handle.read()
            self.log(console, html_buf+"\n")

        self.log(console, "BUILDING REPORT")  # DEBUG

        # If input data is invalid
        #
        if len(invalid_msgs) != 0:
            reportName = 'trf_report_' + str(uuid.uuid4())
            report += "FAILURE\n\n" + "\n".join(invalid_msgs) + "\n"
            reportObj = {
                'objects_created': [],
                'text_message': report
            }
            report_obj_info = ws.save_objects({
                # 'id':info[6],
                'workspace': params['workspace_name'],
                'objects': [
                    {
                        'type': 'KBaseReport.Report',
                        'data': reportObj,
                        'name': reportName,
                        'meta': {},
                        'hidden': 1
                    }
                ]
            })[0]
            returnVal = {'report_name': reportName,
                         'report_ref': str(report_obj_info[6]) + '/' + str(report_obj_info[0]) + '/' + str(
                             report_obj_info[4]),
                         }
            return [returnVal]

        # If input data is VALID
        # Create report obj
        #
        reportName = 'trf_report_'+str(uuid.uuid4())
        reportObj = {'objects_created': [],
                     'message': '',  # or is it 'text_message'?
                     'direct_html': '',
                     'direct_html_link_index': None,
                     'file_links': [mask_file, data_file],
                     'html_links': [html_file],
                     'workspace_name': params['workspace_name'],
                     'report_object_name': reportName
                     }
#        reportObj['objects_created'].append({'ref': str(params['workspace_name'])+'/'+str(html_file),'description': 'Report'})
        reportObj['direct_html_link_index'] = 0

        SERVICE_VER = 'release'
        reportClient = KBaseReport(self.callback_url, token=ctx['token'], service_ver=SERVICE_VER)
        report_info = reportClient.create_extended_report(reportObj)


        # Done
        #
        self.log(console,"BUILDING RETURN OBJECT")
        returnVal = { 'report_name': report_info['name'],
                      'report_ref': report_info['ref'],
                      'output_ref': str(new_obj_info[6])+'/'+str(new_obj_info[0])+'/'+str(new_obj_info[4])
                      }

        self.log(console,"run_TandemRepeats DONE")

        #END tandem_repeats

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method tandem_repeats return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
