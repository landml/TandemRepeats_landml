# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import os
import sys
from Bio import SeqIO
from pprint import pprint, pformat
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from KBaseReport.KBaseReportClient import KBaseReport
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

        ### Construct the command
        #
        #  e.g. trf yoursequence.txt 2 7 7 80 10 50 500 -f -d -m
        #
        trf_cmd = [self.TRF_bin]

        # check for necessary files
        if not os.path.isfile(self.TRF_bin):
            raise ValueError("no such file '" + self.TRF_bin + "'")
        if not os.path.isfile(input_fasta_file):
            raise ValueError("no such file '" + input_fasta_file + "'")
        if not os.path.getsize(input_fasta_file) > 0:
            raise ValueError("empty file '" + input_fasta_file + "'")

        # set the output path
        timestamp = int((datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds() * 1000)
        output_dir = os.path.join(self.scratch, 'output.' + str(timestamp))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_trf_file_path = os.path.join(output_dir, 'tandem_repeats.txt');

        trf_cmd.append(' ' + input_fasta_file + ' 2 7 7 80 10 50 500 -f -d -m')

        # Run Tandem Repeats Finder, capture output as it happens
        #
        self.log(console, 'RUNNING TandemRepeatsFinder:')
        self.log(console, '    ' + ' '.join(trf_cmd))

        # TRF requires shell=True in order to see input data
        env = os.environ.copy()
        #        p = subprocess.Popen(trf_cmd, \
        joined_trf_cmd = ' '.join(trf_cmd)  # redirect out doesn't work with subprocess unless you join command first
        p = subprocess.Popen([joined_trf_cmd], \
                             cwd=self.scratch, \
                             stdin=subprocess.PIPE, \
                             stdout=subprocess.PIPE, \
                             stderr=subprocess.PIPE, \
                             shell=True, \
                             env=env)


        p.wait()


        # Read output
        #
        while True:
            line = p.stdout.readline()
            #line = p.stderr.readline()
            if not line: break
            self.log(console, line.replace('\n', ''))

        p.stdout.close()
        #p.stderr.close()
        p.wait()
        self.log(console, 'return code: ' + str(p.returncode))
        if p.returncode != 0:
            raise ValueError('Error running TandemRepeatsFinder, return code: '+str(p.returncode) +
                '\n\n'+ '\n'.join(console))

        # Check that TandemRepeatsFinder produced output
        #
        if not os.path.isfile(output_trf_file_path):
            raise ValueError("failed to create FASTTREE output: "+output_newick_file_path)
        elif not os.path.getsize(output_trf_file_path) > 0:
            raise ValueError("created empty file for FASTTREE output: "+output_newick_file_path)

        # Upload results
        #
        if len(invalid_msgs) == 0:
            self.log(console,"UPLOADING RESULTS")  # DEBUG


            with open(output_trf_file_path,'r',0) as output_trf_file_handle:
                output_trf_buf = output_trf_file_handle.read()
            output_trf_buf = output_trf_buf.rstrip()
            if not output_trf_buf.endswith(';'):
                output_trf_buf += ';'
            self.log(console, output_trf_buf+"\n")

            # If input data is invalid
            #
        self.log(console, "BUILDING REPORT")  # DEBUG

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

        # Create report obj
        #
        reportName = 'trf_report_'+str(uuid.uuid4())
        reportObj = {'objects_created': [],
                     'message': '',  # or is it 'text_message'?
                     'direct_html': '',
                     'direct_html_link_index': None,
                     'file_links': [],
                     'html_links': [],
                     'workspace_name': params['workspace_name'],
                     'report_object_name': reportName
                     }
        reportObj['objects_created'].append({'ref': str(params['workspace_name'])+'/'+str(params['output_name']),'description': 'Report'})
        reportObj['direct_html_link_index'] = 0

        SERVICE_VER = 'release'
        reportClient = KBaseReport(self.callbackURL, token=ctx['token'], service_ver=SERVICE_VER)
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
