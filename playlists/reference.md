```class CourseGrade():
    student -> FK(student)
    course -> FK(course)

class CourseAttendance():
    student -> FK(student)
    course -> FK(course)
    datetime -> DateTime

class Course():
    students -> M2M()
    # course_obj.coursegrade_set.all()
    # course_obj.Courseattendance_set.all()

class Parent():
    name
    # parent_obj.student_set.all()

class Student():
    mother = FK(parent, related_name='mother')
    father = FK(parent, related_name='father')
    # student.course_set.all()
    # student.coursegrade_set.all()
    # student.father
    # student.mother
```

-------------------------------------

```
playlist_a = Playlist.objects.first()
```

## Add to ManyToMany
```
video_a = Video.object.first()
playlist_a.video.add(video_a)
```

## Remove from ManyToMany
```
video_a = Video.object.first()
playlist_a.video.remove(video_a)
```

## Set (or reset) ManyToMany
```
video_qs = Video.objects.all()
playlist_a.video.set(video_qs)
```

## Clear ManyToMany
```
video_a = Video.objects.all()
playlist_a.videos.clear()
```

## Query from ManyToMany
```
playlist_a.videos.all()
```