📝 Script: FAMILY_extract_info_ENIGMA.py

This script extracts basic FreeSurfer environment and quality information from a directory containing FreeSurfer outputs.

What it produces:
It generates a .csv file with one row per subject, including:
1. subject_dir → subject folder name
2. platform → operating system type (e.g., Linux)
3. platform_version → kernel or OS version (e.g., 5.14.0-427.76.1.el9_4.x86_64)
4. freesurfer_release → exact FreeSurfer build/release string used (e.g., freesurfer-linux-centos8_x86_64-7.3.2-20220804-6354275)
5. lh_surfaceholes → number of surface holes on the left hemisphere (quality check)
6. rh_surfaceholes → number of surface holes on the right hemisphere (quality check)

How to run it:
python3 FAMILY_extract_info_ENIGMA.py \
    --fs_dir <directory_with_freesurfer_output> \
    --out_file <name_of_outputfile.csv>
