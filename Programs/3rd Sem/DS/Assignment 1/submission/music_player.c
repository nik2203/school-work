#include "queue.h"
#include "dll.h"
#include "music_player.h"
#include <stdio.h>
#include <stdlib.h>

playlist_t *create_playlist() // return a newly created doubly linked list
{
	// DO NOT MODIFY!!!
	playlist_t *playlist = (playlist_t *)malloc(sizeof(playlist_t));
	playlist->list = create_list();
	playlist->num_songs = 0;
	playlist->last_song = NULL;
	return playlist;
}

void delete_playlist(playlist_t *playlist) // delete the playlist
{
	// DO NOT MODIFY!!!
	delete_list(playlist->list);
	free(playlist);
}

music_queue_t *create_music_queue() // return a newly created queue
{
	// DO NOT MODIFY!!!
	return create_queue();
}

void clear_music_queue(music_queue_t *q) // clear the queue q
{
	// DO NOT MODIFY!!!
	delete_queue(q);
}

void add_song(playlist_t *playlist, int song_id, int where) // TODO: add a song id to the end of the playlist
{
	if(where == -1){
		insert_front(playlist->list,song_id); // Checking if it's empty and adding from the front
		playlist->num_songs++;
	}
	else if(where == -2){
		insert_back(playlist->list,song_id);//
		playlist->num_songs++;
	}
	else if(where > 0){
		insert_after(playlist->list,song_id,where);
		playlist->num_songs++;
	}
	else{
		return;
	}
}

void delete_song(playlist_t *playlist, int song_id) // TODO: remove song id from the playlist
{
	if(playlist->list->size == 0){
		return;
	}
	else{
		song_t *del = search_song(playlist, song_id); // returns a pointer pointing to that song
		if(del->prev==NULL){
			delete_front(playlist->list); // if it's the only song in the playlist then deleting from the front
		}
		else if(del->next==NULL){
			delete_back(playlist->list); // if there's no other song after it so calling the delete back function
		}
		else{
			delete_node(playlist->list,song_id);
		}
		playlist->list->size--;
		playlist->num_songs--;
	}
}

song_t *search_song(playlist_t *playlist, int song_id) // TODO: return a pointer to the node where the song id is present in the playlist
{
	return search(playlist->list, song_id);
}

void search_and_play(playlist_t *playlist, int song_id) // TODO: play the song with given song_id from the list(no need to bother about the queue. Call to this function should always play the given song and further calls to play_next and play_previous)
{
	song_t *sear = search_song(playlist, song_id); // Making a new node that has the given song
	playlist->last_song=sear;
	if (sear == NULL){
		return;
	}
	else{
		play_song(sear->data); // Playing that song 
	}
}

void play_next(playlist_t *playlist, music_queue_t *q) // TODO: play the next song in the linked list if the queue is empty. If the queue if not empty, play from the queue
{
	if(empty(q)){ // Playing it from the linked list if the queue is empty 
		if(playlist->last_song == NULL || playlist->last_song->next == NULL){
			playlist->last_song = playlist->list->head;
			play_song(playlist->last_song->data);
		}
		else{
			playlist->last_song = playlist->last_song->next;
			play_song(playlist->last_song->data);
		}
		return;
	}
	else{
		play_from_queue(q); // Playing from the queue if it's not empty 
	}
}

void play_previous(playlist_t *playlist) // TODO: play the previous song from the linked list
{
	if(playlist->num_songs!=0){ // Playing the previous song in the linked list
		if(playlist->last_song == NULL || playlist->last_song->prev == NULL){
			playlist->last_song = playlist->list->tail;
			play_song(playlist->last_song->data);
		}
		else{
			playlist->last_song = playlist->last_song->prev;
			play_song(playlist->last_song->data);
		}
	}
	else
		return;
}

void play_from_queue(music_queue_t *q) // TODO: play a song from the queue
{
	int x = dequeue(q);
	play_song(x);
}

void insert_to_queue(music_queue_t *q, int song_id) // TODO: insert a song id to the queue
{
	enqueue(q, song_id);
}

void reverse(playlist_t *playlist) // TODO: reverse the order of the songs in the given playlist. (Swap the nodes, not data)
{
	if(playlist->list->head == NULL){
		return;
	}
	else{
		song_t *cur=playlist->list->head; // making a new node that points to first song
		song_t *swap=playlist->list->head; // this node is used to change the order
		song_t *revtemp=NULL;
		song_t *prev=NULL;

		while(swap->next != NULL){
			cur=swap->next;
			swap->next=swap->prev;
			swap->prev=cur;
			prev=swap;
			swap=cur;
			cur=cur->next;
		}
		swap->next=prev;
		swap->prev=NULL;
		revtemp=playlist->list->head;
		playlist->list->head=playlist->list->tail;
		playlist->list->tail=revtemp;
		return;
	}
}

void k_swap(playlist_t *playlist, int k) // TODO: swap the node at position i with node at position i+k upto the point where i+k is less than the size of the linked list
{
	if(playlist->list->size != 0){
		int i=0, n=playlist->num_songs;
		song_t *swap=playlist->list->head;
		song_t *cur=playlist->list->head;
		for (i=0;i+k<n;i++)
		{
			cur=swap;
			for(int j=0;j<k;j++){
				cur=cur->next;
			}
			//Variables for adjacent nodes of songs to be swapped
			song_t *cnext=cur->next;
			song_t *sprev=swap->prev;
			song_t *cprev=cur->prev;
			song_t *snext=swap->next;

			if(k == 1){
				cprev = cur;
				snext = swap;
			}

			cur->next = snext;
			cur->prev = sprev;
			swap->next = cnext;
			swap->prev = cprev;

			if(snext!=NULL){
				snext->prev = cur;
			}
			if(cnext!=NULL){
				cnext->prev = swap;
			}
			if(cprev!=NULL){
				cprev->next = swap;
			}
			if(swap==playlist->list->head){
				playlist->list->head=cur;
			}
			else{
				sprev->next = cur;
			}
			swap = snext;
		}
		song_t *last=playlist->list->head;
		while(last->next != NULL){
			last=last->next;
		}
		playlist->list->tail=last;
	}
}

void shuffle(playlist_t *playlist, int k) // TODO: perform k_swap and reverse
{
	k_swap(playlist, k); // randomly shuffles the playlist
	reverse(playlist);
}

song_t *debug(playlist_t *playlist) // TODO: if the given linked list has a cycle, return the start of the cycle, else return null. Check cycles only in forward direction i.e with the next pointer. No need to check for cycles in the backward pointer.
{
	song_t *last = playlist->list->tail->next;
	return last;
}

void display_playlist(playlist_t *p) // Displays the playlist
{
	// DO NOT MODIFY!!!
	display_list(p->list);
}

void play_song(int song_id)
{
	// DO NOT MODIFY!!!
	printf("Playing: %d\n", song_id);
}