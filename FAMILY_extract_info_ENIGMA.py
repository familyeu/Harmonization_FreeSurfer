import os
import re
import csv
import argparse
import logging

def search_info(file_path,keyword):
    with open(file_path,'r') as file:
        for line in file:
            if keyword in line:
                break
    return line


def subtract_info(path,out_file):
    logging.info(f"Subtracting information from freesurfer output")    
    sub_dirs = [s for s in os.listdir(path) if os.path.isdir(os.path.join(path,s)) and 'sub' in s]
    logging.info(f"Number of subject-directories found: {len(sub_dirs)}")

    if os.path.exists(out_file):
        logging.info(f"File with filename {out_file} already exists, choose a different name. Exiting.")
        exit()

    logging.info(f"Writing to file: {out_file}") 
    with open(out_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["subject_dir","platform","platform_version","freesurfer_release","lh_surfaceholes","rh_surfaceholes"])

        for sub in sub_dirs:
            try:
                # Kernel
                path_recon = os.path.join(path,sub,'scripts/recon-all.log')
                kernel = search_info(path_recon,'Platform')
                platform = re.search(r'Platform:\s*([^\s,]+)',kernel).group(1)
                version = re.search(r'PlatformVersion:\s*([^\s,]+)',kernel).group(1)
            except:
                platform = 'NA'
                version = 'NA'

            try:
                # Freesurfer release
                path_stamp = os.path.join(path,sub,'scripts/build-stamp.txt')
                release = search_info(path_stamp,'freesurfer').strip()
            except:
                release = 'NA'

            try:
                # Euler numbers
                path_stats = os.path.join(path,sub,'stats/aseg.stats')
                lh_sh = search_info(path_stats,'lhSurfaceHoles')
                lh_sh = re.search(r'\d+', lh_sh).group()
     
                rh_sh = search_info(path_stats,'rhSurfaceHoles')
                rh_sh = re.search(r'\d+', rh_sh).group()
            except:
                lh_sh = 'NA'
                rh_sh = 'NA'

            # Write to file
            writer.writerow([sub,platform,version,release,lh_sh,rh_sh])
            logging.info(f"Info from subject-directory {sub} was written to output-file")
        
        logging.info(f"Information from {len(sub_dirs)} subjects was written to file {out_file}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='Obtain kernel, freesurfer version and Euler numbers')
    parser.add_argument('--fs_dir', type=str, required=True, help='Freesurfer output directory')
    parser.add_argument('--out_file', type=str, required=True, help='Filename outputfile')
    args = parser.parse_args()
    subtract_info(args.fs_dir,args.out_file)
