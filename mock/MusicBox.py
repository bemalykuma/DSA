class Song:
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = int(durations)
        self.next = None
    
    def show_info(self):
        mi = self.durations // 60
        sec = self.durations - mi*60
        if sec < 10:
            sec = "0"+str(sec)
        return self.name + " <|> " + self.genre + " <|> " + str(mi)+"."+str(sec)

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        self.data = None

    def enqueue(self, item: "Song"):
        new = Song(item.name, item.genre, item.durations)
        if self.isEmpty():
            self.data = new
        else:
            start = self
            while start.rear != None:
                start = start.rear
            new = start.rear
            
        self.count += 1
        return

    def dequeue(self):
        if self.isEmpty():
            print("Underflow! Dequeue from an empty queue")
        else:
            if self.count > 1:
                self.data = self.rear
            else:
                self.data = None
            self.count -= 1
        return

    def peek(self):
        if self.isEmpty():
            print("Underflow! peek from an empty queue")
        else:
            return self.head

    def isEmpty(self):
        if self.data is None:
            return True
        return False

    def show_Queue(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            start = self.data
            for i in range(1,self.count+1):
                print("Queue#"+str(i),start.show_info())
                start = start.next

    def lastSong(self):
        pass
    def removeSong(self):
        pass
    def groupSong(self):
        pass
    def undo(self):
        pass
    def rev_queue(self):
        pass

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()