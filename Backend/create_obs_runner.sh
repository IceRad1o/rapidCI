#!/bin/bash

repo_url=$1
repo_name=$2
localFolder="../Git_repo/"

obs_folder="$localFolder""$repo_name""_obs"
runner_folder="$localFolder""$repo_name""_runner"
# echo "$obs_folder"
git clone "$repo_url" "$obs_folder"
git clone "$repo_url" "$runner_folder"



