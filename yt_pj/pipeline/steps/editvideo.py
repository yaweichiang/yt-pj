from moviepy.editor import VideoFileClip, concatenate_videoclips
from yt_pj.pipeline.steps.step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        print('剪輯影片')
        videos = []
        cutfounds = []
        for found in data:
            video_path = found.yt.video_path
            if not utils.video_exist(found.yt):
                continue

            start_t, end_t = self.get_real_time(found.time)
            print(start_t, end_t)
            cutfounds.append(found)

            video = VideoFileClip(video_path).subclip(start_t, end_t)
            videos.append(video)
            if len(videos) == inputs['limit']:
                break

        clips = concatenate_videoclips(videos)
        clips.write_videofile(utils.get_outputs_path(inputs), audio_codec='aac')
        return cutfounds

    @staticmethod
    def get_real_time(time):
        real_time = time.split(' --> ')
        return '.'.join(real_time[0].split(',')), '.'.join(real_time[-1].split(','))
