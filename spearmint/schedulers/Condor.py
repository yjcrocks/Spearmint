# -*- coding: utf-8 -*-
# Spearmint
#
# Academic and Non-Commercial Research Use Software License and Terms
# of Use
#
# Spearmint is a software package to perform Bayesian optimization
# according to specific algorithms (the ��Software��).  The Software is
# designed to automatically run experiments (thus the code name
# 'spearmint') in a manner that iteratively adjusts a number of
# parameters so as to minimize some objective in as few runs as
# possible.
#
# The Software was developed by Ryan P. Adams, Michael Gelbart, and
# Jasper Snoek at Harvard University, Kevin Swersky at the
# University of Toronto (��Toronto��), and Hugo Larochelle at the
# Universit�� de Sherbrooke (��Sherbrooke��), which assigned its rights
# in the Software to Socpra Sciences et G��nie
# S.E.C. (��Socpra��). Pursuant to an inter-institutional agreement
# between the parties, it is distributed for free academic and
# non-commercial research use by the President and Fellows of Harvard
# College (��Harvard��).
#
# Using the Software indicates your agreement to be bound by the terms
# of this Software Use Agreement (��Agreement��). Absent your agreement
# to the terms below, you (the ��End User��) have no rights to hold or
# use the Software whatsoever.
#
# Harvard agrees to grant hereunder the limited non-exclusive license
# to End User for the use of the Software in the performance of End
# User��s internal, non-commercial research and academic use at End
# User��s academic or not-for-profit research institution
# (��Institution��) on the following terms and conditions:
#
# 1.  NO REDISTRIBUTION. The Software remains the property Harvard,
# Toronto and Socpra, and except as set forth in Section 4, End User
# shall not publish, distribute, or otherwise transfer or make
# available the Software to any other party.
#
# 2.  NO COMMERCIAL USE. End User shall not use the Software for
# commercial purposes and any such use of the Software is expressly
# prohibited. This includes, but is not limited to, use of the
# Software in fee-for-service arrangements, core facilities or
# laboratories or to provide research services to (or in collaboration
# with) third parties for a fee, and in industry-sponsored
# collaborative research projects where any commercial rights are
# granted to the sponsor. If End User wishes to use the Software for
# commercial purposes or for any other restricted purpose, End User
# must execute a separate license agreement with Harvard.
#
# Requests for use of the Software for commercial purposes, please
# contact:
#
# Office of Technology Development
# Harvard University
# Smith Campus Center, Suite 727E
# 1350 Massachusetts Avenue
# Cambridge, MA 02138 USA
# Telephone: (617) 495-3067
# Facsimile: (617) 495-9568
# E-mail: otd@harvard.edu
#
# 3.  OWNERSHIP AND COPYRIGHT NOTICE. Harvard, Toronto and Socpra own
# all intellectual property in the Software. End User shall gain no
# ownership to the Software. End User shall not remove or delete and
# shall retain in the Software, in any modifications to Software and
# in any Derivative Works, the copyright, trademark, or other notices
# pertaining to Software as provided with the Software.
#
# 4.  DERIVATIVE WORKS. End User may create and use Derivative Works,
# as such term is defined under U.S. copyright laws, provided that any
# such Derivative Works shall be restricted to non-commercial,
# internal research and academic use at End User��s Institution. End
# User may distribute Derivative Works to other Institutions solely
# for the performance of non-commercial, internal research and
# academic use on terms substantially similar to this License and
# Terms of Use.
#
# 5.  FEEDBACK. In order to improve the Software, comments from End
# Users may be useful. End User agrees to provide Harvard with
# feedback on the End User��s use of the Software (e.g., any bugs in
# the Software, the user experience, etc.).  Harvard is permitted to
# use such information provided by End User in making changes and
# improvements to the Software without compensation or an accounting
# to End User.
#
# 6.  NON ASSERT. End User acknowledges that Harvard, Toronto and/or
# Sherbrooke or Socpra may develop modifications to the Software that
# may be based on the feedback provided by End User under Section 5
# above. Harvard, Toronto and Sherbrooke/Socpra shall not be
# restricted in any way by End User regarding their use of such
# information.  End User acknowledges the right of Harvard, Toronto
# and Sherbrooke/Socpra to prepare, publish, display, reproduce,
# transmit and or use modifications to the Software that may be
# substantially similar or functionally equivalent to End User��s
# modifications and/or improvements if any.  In the event that End
# User obtains patent protection for any modification or improvement
# to Software, End User agrees not to allege or enjoin infringement of
# End User��s patent against Harvard, Toronto or Sherbrooke or Socpra,
# or any of the researchers, medical or research staff, officers,
# directors and employees of those institutions.
#
# 7.  PUBLICATION & ATTRIBUTION. End User has the right to publish,
# present, or share results from the use of the Software.  In
# accordance with customary academic practice, End User will
# acknowledge Harvard, Toronto and Sherbrooke/Socpra as the providers
# of the Software and may cite the relevant reference(s) from the
# following list of publications:
#
# Practical Bayesian Optimization of Machine Learning Algorithms
# Jasper Snoek, Hugo Larochelle and Ryan Prescott Adams
# Neural Information Processing Systems, 2012
#
# Multi-Task Bayesian Optimization
# Kevin Swersky, Jasper Snoek and Ryan Prescott Adams
# Advances in Neural Information Processing Systems, 2013
#
# Input Warping for Bayesian Optimization of Non-stationary Functions
# Jasper Snoek, Kevin Swersky, Richard Zemel and Ryan Prescott Adams
# Preprint, arXiv:1402.0929, http://arxiv.org/abs/1402.0929, 2013
#
# Bayesian Optimization and Semiparametric Models with Applications to
# Assistive Technology Jasper Snoek, PhD Thesis, University of
# Toronto, 2013
#
# 8.  NO WARRANTIES. THE SOFTWARE IS PROVIDED "AS IS." TO THE FULLEST
# EXTENT PERMITTED BY LAW, HARVARD, TORONTO AND SHERBROOKE AND SOCPRA
# HEREBY DISCLAIM ALL WARRANTIES OF ANY KIND (EXPRESS, IMPLIED OR
# OTHERWISE) REGARDING THE SOFTWARE, INCLUDING BUT NOT LIMITED TO ANY
# IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE, OWNERSHIP, AND NON-INFRINGEMENT.  HARVARD, TORONTO AND
# SHERBROOKE AND SOCPRA MAKE NO WARRANTY ABOUT THE ACCURACY,
# RELIABILITY, COMPLETENESS, TIMELINESS, SUFFICIENCY OR QUALITY OF THE
# SOFTWARE.  HARVARD, TORONTO AND SHERBROOKE AND SOCPRA DO NOT WARRANT
# THAT THE SOFTWARE WILL OPERATE WITHOUT ERROR OR INTERRUPTION.
#
# 9.  LIMITATIONS OF LIABILITY AND REMEDIES. USE OF THE SOFTWARE IS AT
# END USER��S OWN RISK. IF END USER IS DISSATISFIED WITH THE SOFTWARE,
# ITS EXCLUSIVE REMEDY IS TO STOP USING IT.  IN NO EVENT SHALL
# HARVARD, TORONTO OR SHERBROOKE OR SOCPRA BE LIABLE TO END USER OR
# ITS INSTITUTION, IN CONTRACT, TORT OR OTHERWISE, FOR ANY DIRECT,
# INDIRECT, SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR OTHER
# DAMAGES OF ANY KIND WHATSOEVER ARISING OUT OF OR IN CONNECTION WITH
# THE SOFTWARE, EVEN IF HARVARD, TORONTO OR SHERBROOKE OR SOCPRA IS
# NEGLIGENT OR OTHERWISE AT FAULT, AND REGARDLESS OF WHETHER HARVARD,
# TORONTO OR SHERBROOKE OR SOCPRA IS ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGES.
#
# 10. INDEMNIFICATION. To the extent permitted by law, End User shall
# indemnify, defend and hold harmless Harvard, Toronto and Sherbrooke
# and Socpra, their corporate affiliates, current or future directors,
# trustees, officers, faculty, medical and professional staff,
# employees, students and agents and their respective successors,
# heirs and assigns (the "Indemnitees"), against any liability,
# damage, loss or expense (including reasonable attorney's fees and
# expenses of litigation) incurred by or imposed upon the Indemnitees
# or any one of them in connection with any claims, suits, actions,
# demands or judgments arising from End User��s breach of this
# Agreement or its Institution��s use of the Software except to the
# extent caused by the gross negligence or willful misconduct of
# Harvard, Toronto or Sherbrooke or Socpra. This indemnification
# provision shall survive expiration or termination of this Agreement.
#
# 11. GOVERNING LAW. This Agreement shall be construed and governed by
# the laws of the Commonwealth of Massachusetts regardless of
# otherwise applicable choice of law standards.
#
# 12. NON-USE OF NAME.  Nothing in this License and Terms of Use shall
# be construed as granting End Users or their Institutions any rights
# or licenses to use any trademarks, service marks or logos associated
# with the Software.  You may not use the terms ��Harvard�� or
# ��University of Toronto�� or ��Universit�� de Sherbrooke�� or ��Socpra
# Sciences et G��nie S.E.C.�� (or a substantially similar term) in any
# way that is inconsistent with the permitted uses described
# herein. You agree not to use any name or emblem of Harvard, Toronto
# or Sherbrooke, or any of their subdivisions for any purpose, or to
# falsely suggest any relationship between End User (or its
# Institution) and Harvard, Toronto and/or Sherbrooke, or in any
# manner that would infringe or violate any of their rights.
#
# 13. End User represents and warrants that it has the legal authority
# to enter into this License and Terms of Use on behalf of itself and
# its Institution.

import classad
import htcondor
import os
import re
import shlex
import shutil
import socket
import spearmint
import subprocess
import sys

from abstract_scheduler import AbstractScheduler
from string import Template

def init(*args, **kwargs):
    return CondorScheduler(*args, **kwargs)

class CondorScheduler(AbstractScheduler):
    """scheduler which submits jobs to the htcondor via a shell command"""

    def submit(self, job_id, experiment_name, experiment_dir, database_address):
        base_path = os.path.dirname(os.path.realpath(spearmint.__file__))

        # Since "localhost" might mean something different on the machine
        # we are submitting to, set it to the actual name of the parent machine
        if database_address == 'localhost':
            database_address = socket.gethostname()

        python_location = sys.executable
        if not python_location:
	    python_location = '/home/ugrd_yjchang/anaconda2/bin/python'

        run_command = '#!/bin/bash\n'
        if 'environment-file' in self.options:
            run_command += 'source %s\n' % self.options['environment-file']
        run_command += 'cd %s\n' % base_path
        run_command += '%s launcher.py --database-address=%s --experiment-name=%s --job-id=%s %s\n' % \
               (python_location, database_address, experiment_name, job_id, experiment_dir)

        # remove executables after execution
        run_command += '\n# Delete executables\n'
        run_command += 'FILE_NAME=$(basename "$0")\n'
        run_command += 'DIR_PATH=$(cd $(dirname "$0") && pwd -P)\n'
        run_command += 'JOB_NAME=$(echo $FILE_NAME | cut -f 1 -d ".")\n\n'
        run_command += 'rm $DIR_PATH/$JOB_NAME.sub\n'
        run_command += 'rm $DIR_PATH/$FILE_NAME\n'

        if 'scheduler-args' in self.options:
            warn("HTCondor does not support scheduler-args")

        output_directory = os.path.join(experiment_dir, 'output')
        if not os.path.isdir(output_directory):
            os.mkdir(output_directory)

        if 'output-subdir' in self.options:
            output_directory = os.path.join(output_directory, self.options['output-subdir'])
            if not os.path.isdir(output_directory):
                os.mkdir(output_directory)

        output_filename = os.path.join(output_directory, '%08d.out' % job_id)
        error_filename  = os.path.join(output_directory, '%08d.err' % job_id)
        log_filename    = os.path.join(output_directory, '%08d.log' % job_id)

        # build temp directory
        temp_dir = os.path.join(experiment_dir, '.tempSubFiles')
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)

        # build executable
        executable = '%s_%08d.sh' % (experiment_name, job_id)
        executable_path = os.path.join(temp_dir, executable)
        with open(executable_path, 'w') as f:
           f.write(run_command)
        st = os.stat(executable_path)
        os.chmod(executable_path, st.st_mode | 0o111)

        # prepare template (copy template into expr_dir if not given)
        template_path = os.path.join(experiment_dir, '%s.sub.template' % experiment_name)
        if not os.path.isfile(template_path):
            sample_template_path = \
                os.path.join(os.path.join(base_path, 'schedulers'), 'condor.sub.template')
            shutil.copyfile(sample_template_path, template_path)

        # build submit file
        submit_filename = '%s_%08d.sub' % (experiment_name, job_id)
        submit_filepath = os.path.join(temp_dir, submit_filename)
        with open(submit_filepath, 'w') as f:
            replace_dict = {
                'error_filename': error_filename,
                'executable': executable,
                'executable_path': executable_path,
                'experiment_name': experiment_name,
                'experiment_dir': experiment_dir,
                'log_filename': log_filename,
                'output_filename': output_filename,
                'run_command': run_command,
                'submit_filename': submit_filename,
            }
            with open(template_path, 'r') as template_file:
                template = Template(template_file.read())
            submit_file_content = template.substitute(replace_dict)
            f.write(submit_file_content)

        # submit into htcondor
        process = subprocess.Popen(
            'condor_submit %s' % submit_filepath,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True
        )
        output, std_err = process.communicate()

        # parse out the cluster id from command output
        match = re.search(r'submitted to cluster (\d+)', output)
        try:
            return int(match.group(1))
        except:
            sys.stderr.write(output)
            return None


    def alive(self, cluster_id):
        schedd = htcondor.Schedd()
        result_ads = schedd.query('ClusterId =?= %d' % cluster_id)
        return len(result_ads) > 0
